"""
Familien-Speiseplan Integration für Home Assistant
"""
import json
import logging
import os
from pathlib import Path

from homeassistant.components import frontend
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import CoreState, HomeAssistant, ServiceCall, Event
from homeassistant.helpers.typing import ConfigType

DOMAIN = "speiseplan"
DATA_FILE = "speiseplan_data.json"
PANEL_URL = "speiseplan"

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


def _register_panel(hass: HomeAssistant) -> None:
    """Register the sidebar panel, if not already registered."""
    if PANEL_URL in hass.data.get("frontend_panels", {}):
        return
    try:
        frontend.async_register_built_in_panel(
            hass,
            component_name="iframe",
            sidebar_title="Speiseplan",
            sidebar_icon="mdi:silverware-fork-knife",
            frontend_url_path=PANEL_URL,
            config={"url": "/local/speiseplan.html"},
            require_admin=False,
        )
        _LOGGER.info("Speiseplan: Sidebar-Panel registriert")
    except ValueError:
        # Panel already registered (e.g. reload)
        pass


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
        # Use executor to avoid blocking the event loop
        await hass.async_add_executor_job(
            shutil.copy2, html_source, html_destination
        )
        _LOGGER.info("Copied speiseplan.html to www directory")
    except Exception as err:
        _LOGGER.error("Failed to copy HTML file: %s", err)

    # Register sidebar panel once the frontend is ready
    if hass.state is CoreState.running:
        _register_panel(hass)
    else:
        # Fehlerbehebung: Da Home Assistant 'homeassistant_started' im SyncWorker ausführen kann,
        # zwingen wir den Aufruf über eine asynchrone Funktion zurück in den Haupt-Event-Loop.
        async def _async_register_panel_event(_event: Event) -> None:
            _register_panel(hass)

        hass.bus.async_listen_once(
            "homeassistant_started", _async_register_panel_event
        )
    
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

    # Remove sidebar panel
    try:
        frontend.async_remove_panel(hass, PANEL_URL)
    except Exception:
        pass
    
    _LOGGER.info("Speiseplan integration unloaded")
    
    return True
def _register_panel(hass: HomeAssistant) -> None:
    """Register the sidebar panel, if not already registered."""
    if PANEL_URL in hass.data.get("frontend_panels", {}):
        return
    try:
        frontend.async_register_built_in_panel(
            hass,
            component_name="iframe",
            sidebar_title="Speiseplan",
            sidebar_icon="mdi:silverware-fork-knife",
            frontend_url_path=PANEL_URL,
            config={"url": "/local/speiseplan.html"},
            require_admin=False,
        )
        _LOGGER.info("Speiseplan: Sidebar-Panel registriert")
    except ValueError:
        # Panel already registered (e.g. reload)
        pass


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
        # Use executor to avoid blocking the event loop
        await hass.async_add_executor_job(
            shutil.copy2, html_source, html_destination
        )
        _LOGGER.info("Copied speiseplan.html to www directory")
    except Exception as err:
        _LOGGER.error("Failed to copy HTML file: %s", err)

    # Register sidebar panel once the frontend is ready
    if hass.state is CoreState.running:
        _register_panel(hass)
    else:
        hass.bus.async_listen_once(
            "homeassistant_started", lambda _event: _register_panel(hass)
        )
    
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

    # Remove sidebar panel
    try:
        frontend.async_remove_panel(hass, PANEL_URL)
    except Exception:
        pass
    
    _LOGGER.info("Speiseplan integration unloaded")
    
    return True
