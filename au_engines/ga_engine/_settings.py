from .base import Base, HttpMethod

class Settings(Base):

    def get_settings(self) -> dict | None:
        """Get the current settings of the instance."""
        return self.call_instance_api("getSettings")
    
    def get_state(self) -> str | None:
        """
        Get the current state of the instance.

        - notAuthorized - free instance
        - authorized
        - blocked
        - starting
        - yellowCard

        - None - does not exists
        """
        response = self.call_instance_api("getStateInstance", http_method=HttpMethod.GET)
        if response is None:
            return None
        return response.get("stateInstance", None)