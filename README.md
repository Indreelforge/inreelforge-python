# InReelForge — Python SDK

[![PyPI version](https://img.shields.io/pypi/v/inreelforge.svg)](https://pypi.org/project/inreelforge/)
[![Python versions](https://img.shields.io/pypi/pyversions/inreelforge.svg)](https://pypi.org/project/inreelforge/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Official Python SDK for the [InReelForge](https://indreelforge.com) Social Media API. Upload videos, photos, and text to **Instagram, YouTube, TikTok, Facebook, X (Twitter), LinkedIn, Threads, Pinterest, Reddit & Bluesky** with a single API call.

## Installation

```bash
pip install inreelforge
```

## Quick Start

```python
from inreelforge import InReelForge

client = InReelForge(api_key="your-api-key-here")

# Upload a video to multiple platforms
result = client.upload_video(
    user="my-profile",
    platforms=["instagram", "tiktok", "youtube"],
    video_path="./my-video.mp4",
    title="Check out this amazing video!",
)

print(result)
# {'status': 'success', 'data': {'upload_id': '...', 'platforms': [...]}}
```

## Features

- **One API call, all platforms** — Upload to 10+ social networks simultaneously
- **Video, Photo & Text** — Support for all content types
- **Scheduling** — Schedule posts for any future date/time
- **Analytics** — Track performance across all platforms
- **Profile Management** — Manage multiple social media accounts
- **Type hints** — Full type annotations for IDE support
- **Lightweight** — Only depends on `requests`

## Usage

### Upload Video

```python
result = client.upload_video(
    user="my-profile",
    platforms=["instagram", "tiktok", "youtube", "facebook"],
    video_path="./video.mp4",
    title="My awesome video",
    first_comment="#socialmedia #viral",
    schedule="2026-04-15T10:00:00Z",
    youtube_privacy="public",
    youtube_tags="tutorial,tech",
)
```

### Upload Photos

```python
result = client.upload_photos(
    user="my-profile",
    platforms=["instagram", "facebook", "pinterest"],
    photo_paths=["./photo1.jpg", "./photo2.jpg"],
    title="Photo carousel",
)
```

### Upload Text

```python
result = client.upload_text(
    user="my-profile",
    platforms=["x", "threads", "bluesky"],
    title="Just shipped a new feature! 🚀",
)
```

### Manage Profiles

```python
# List profiles
data = client.get_profiles()
print(data["profiles"])

# Create profile
client.create_profile("brand-account")

# Delete profile
client.delete_profile("old-account")
```

### Analytics

```python
analytics = client.get_analytics("30d")
print(analytics["total_views"], analytics["engagement_rate"])
```

## Supported Platforms

| Platform | Video | Photo | Text | Scheduling |
|----------|-------|-------|------|------------|
| Instagram | ✓ | ✓ | - | ✓ |
| YouTube | ✓ | - | - | ✓ |
| TikTok | ✓ | ✓ | - | ✓ |
| Facebook | ✓ | ✓ | ✓ | ✓ |
| X (Twitter) | ✓ | ✓ | ✓ | ✓ |
| LinkedIn | ✓ | ✓ | ✓ | ✓ |
| Threads | - | ✓ | ✓ | ✓ |
| Pinterest | - | ✓ | - | ✓ |
| Reddit | ✓ | ✓ | ✓ | ✓ |
| Bluesky | - | ✓ | ✓ | ✓ |

## Error Handling

```python
from inreelforge import InReelForge, InReelForgeError

try:
    result = client.upload_video(...)
except InReelForgeError as e:
    print(f"API Error ({e.status_code}): {e}")
except FileNotFoundError as e:
    print(f"File not found: {e}")
```

## Links

- [Website](https://indreelforge.com)
- [API Documentation](https://indreelforge.com/docs)
- [Dashboard](https://indreelforge.com/dashboard)
- [Pricing](https://indreelforge.com/pricing)
- [Status](https://indreelforge.com/status)
- [Node.js SDK](https://www.npmjs.com/package/inreelforge)

## License

MIT
