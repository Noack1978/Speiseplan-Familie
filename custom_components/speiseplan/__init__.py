"""
Familien-Speiseplan Integration für Home Assistant
"""
import json
import logging
import os
from pathlib import Path

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.typing import ConfigType

DOMAIN = "speiseplan"
DATA_FILE = "speiseplan_data.json"

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Speiseplan component from YAML."""
    
    # Support both YAML and UI config
    if DOMAIN in config:
        _LOGGER.info("Speiseplan: Loading with configuration from YAML")
        # Import as config entry
        hass.async_create_task(
            hass.config_entries.flow.async_init(
                DOMAIN, context={"source": "import"}, data={}
            )
        )
    
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Speiseplan from a config entry."""
    
    _LOGGER.info("Speiseplan: Setting up integration")
    
    # Path to data file in www directory (accessible via /local/)
    www_path = Path(hass.config.path("www"))
    www_path.mkdir(exist_ok=True)
    data_file_path = www_path / DATA_FILE
    
    # Initialize empty file if it doesn't exist
    if not data_file_path.exists():
        data_file_path.write_text("{}")
        _LOGGER.info("Created empty speiseplan data file")
    
    # Copy HTML file from integration to www directory
    # This makes it accessible at /local/speiseplan.html
    integration_path = Path(__file__).parent
    html_source = integration_path / "www" / "speiseplan.html"
    html_destination = www_path / "speiseplan.html"
    
    try:
        import shutil
        shutil.copy2(html_source, html_destination)
        _LOGGER.info("Copied speiseplan.html to www directory")
    except Exception as err:
        _LOGGER.error("Failed to copy HTML file: %s", err)
    
    async def handle_save(call: ServiceCall) -> None:
        """Handle the save service call."""
        try:
            data = call.data.get("data", {})
            
            # Parse if string, otherwise use as-is
            if isinstance(data, str):
                data = json.loads(data)
            
            # Write to file
            await hass.async_add_executor_job(
                data_file_path.write_text, json.dumps(data, indent=2, ensure_ascii=False)
            )
            
            _LOGGER.info("Speiseplan data saved successfully")
            
        except Exception as err:
            _LOGGER.error("Error saving speiseplan data: %s", err)
    
    async def handle_load(call: ServiceCall) -> None:
        """Handle the load service call."""
        try:
            content = await hass.async_add_executor_job(data_file_path.read_text)
            data = json.loads(content)
            
            # Store in hass.data for potential future use
            hass.data[DOMAIN] = data
            
            _LOGGER.info("Speiseplan data loaded successfully")
            
        except Exception as err:
            _LOGGER.error("Error loading speiseplan data: %s", err)
    
    # Register services
    hass.services.async_register(DOMAIN, "save", handle_save)
    hass.services.async_register(DOMAIN, "load", handle_load)
    
    _LOGGER.info("Speiseplan integration loaded")
    
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    
    # Remove services
    hass.services.async_remove(DOMAIN, "save")
    hass.services.async_remove(DOMAIN, "load")
    
    _LOGGER.info("Speiseplan integration unloaded")
    
    return True
