"""InReelForge API client."""

import os
from typing import Any, Dict, List, Optional

import requests


class InReelForgeError(Exception):
    """Error from the InReelForge API."""

    def __init__(self, message: str, status_code: int = 0):
        super().__init__(message)
        self.status_code = status_code


class InReelForge:
    """
    Official Python client for the InReelForge Social Media API.

    Upload videos, photos, and text to Instagram, YouTube, TikTok, Facebook,
    X (Twitter), LinkedIn, Threads, Pinterest, Reddit & Bluesky.

    Args:
        api_key: Your InReelForge API key (required)
        base_url: API base URL (default: https://api.indreelforge.com)
        timeout: Request timeout in seconds (default: 120)

    Example:
        >>> client = InReelForge(api_key="your-api-key")
        >>> result = client.upload_video(
        ...     user="my-profile",
        ...     platforms=["instagram", "tiktok"],
        ...     video_path="./video.mp4",
        ...     title="My video",
        ... )
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.indreelforge.com",
        timeout: int = 120,
    ):
        if not api_key:
            raise ValueError("api_key is required")
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._session = requests.Session()
        self._session.headers.update({"Authorization": f"Apikey {self.api_key}"})

    def _request(
        self,
        method: str,
        path: str,
        json: Optional[Dict] = None,
        data: Optional[Dict] = None,
        files: Optional[Dict] = None,
    ) -> Dict[str, Any]:
        """Make an API request."""
        url = f"{self.base_url}{path}"
        try:
            resp = self._session.request(
                method,
                url,
                json=json,
                data=data,
                files=files,
                timeout=self.timeout,
            )
        except requests.exceptions.Timeout:
            raise InReelForgeError("Request timed out", 408)
        except requests.exceptions.ConnectionError:
            raise InReelForgeError("Connection failed", 0)

        if not resp.ok:
            try:
                err = resp.json().get("error", f"HTTP {resp.status_code}")
            except Exception:
                err = f"HTTP {resp.status_code}"
            raise InReelForgeError(err, resp.status_code)

        return resp.json()

    # ── Upload ──

    def upload_video(
        self,
        user: str,
        platforms: List[str],
        video_path: str,
        title: Optional[str] = None,
        first_comment: Optional[str] = None,
        schedule: Optional[str] = None,
        timezone: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Upload a video to one or more platforms.

        Args:
            user: Profile name (managed user)
            platforms: List of platforms (e.g. ["instagram", "tiktok", "youtube"])
            video_path: Path to the video file
            title: Post title/caption (optional)
            first_comment: First comment text (optional)
            schedule: ISO datetime for scheduling (optional)
            timezone: Timezone for scheduling (optional)
            **kwargs: Platform-specific options (instagram_title, youtube_tags, etc.)

        Returns:
            Upload response with upload_id and platform statuses
        """
        if not os.path.isfile(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")

        data = self._build_form_data(user, platforms, title, first_comment, schedule, timezone, **kwargs)
        files = {"video": (os.path.basename(video_path), open(video_path, "rb"))}

        return self._request("POST", "/api/upload", data=data, files=files)

    def upload_photos(
        self,
        user: str,
        platforms: List[str],
        photo_paths: List[str],
        title: Optional[str] = None,
        first_comment: Optional[str] = None,
        schedule: Optional[str] = None,
        timezone: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Upload photos to one or more platforms.

        Args:
            user: Profile name
            platforms: List of platforms
            photo_paths: List of file paths to photos
            title: Post title/caption (optional)
        """
        data = self._build_form_data(user, platforms, title, first_comment, schedule, timezone, **kwargs)
        files = [("photos[]", (os.path.basename(p), open(p, "rb"))) for p in photo_paths]

        return self._request("POST", "/api/upload_photos", data=data, files=files)

    def upload_text(
        self,
        user: str,
        platforms: List[str],
        title: str,
        first_comment: Optional[str] = None,
        schedule: Optional[str] = None,
        timezone: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Upload a text-only post to one or more platforms.

        Args:
            user: Profile name
            platforms: List of platforms
            title: Text content (required)
        """
        data = self._build_form_data(user, platforms, title, first_comment, schedule, timezone, **kwargs)
        return self._request("POST", "/api/upload_text", data=data)

    def _build_form_data(
        self,
        user: str,
        platforms: List[str],
        title: Optional[str] = None,
        first_comment: Optional[str] = None,
        schedule: Optional[str] = None,
        timezone: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        data: Dict[str, Any] = {"user": user, "platform[]": platforms}
        if title:
            data["title"] = title
        if first_comment:
            data["first_comment"] = first_comment
        if schedule:
            data["schedule"] = schedule
        if timezone:
            data["timezone"] = timezone
        for key, value in kwargs.items():
            data[key] = value
        return data

    # ── Profiles ──

    def get_profiles(self) -> Dict[str, Any]:
        """List all managed profiles."""
        return self._request("GET", "/api/profiles")

    def create_profile(self, name: str) -> Dict[str, Any]:
        """Create a new managed profile."""
        return self._request("POST", "/api/profiles", json={"name": name})

    def delete_profile(self, name: str) -> Dict[str, Any]:
        """Delete a managed profile."""
        return self._request("DELETE", f"/api/profiles/{name}")

    # ── Analytics ──

    def get_analytics(self, range: str = "30d") -> Dict[str, Any]:
        """Get analytics overview."""
        return self._request("GET", f"/api/analytics/overview?range={range}")

    # ── Plans ──

    def get_plans(self) -> Dict[str, Any]:
        """List available subscription plans."""
        return self._request("GET", "/api/plans")
