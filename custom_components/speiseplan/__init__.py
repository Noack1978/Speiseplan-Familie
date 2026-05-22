"""
Familien-Speiseplan Integration für Home Assistant
"""
import json
import logging
import os
from pathlib import Path

from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers.typing import ConfigType

DOMAIN = "speiseplan"
DATA_FILE = "speiseplan_data.json"

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Speiseplan component."""
    
    # Path to data file in www directory (accessible via /local/)
    www_path = Path(hass.config.path("www"))
    www_path.mkdir(exist_ok=True)
    data_file_path = www_path / DATA_FILE
    
    # Initialize empty file if it doesn't exist
    if not data_file_path.exists():
        data_file_path.write_text("{}")
        _LOGGER.info("Created empty speiseplan data file")
    
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
