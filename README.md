# Discord File Updater (DFU)

Automatically download and manage files from Discord channels with ease.

## Overview

Discord File Updater is a powerful Python bot that monitors specified Discord channels (both text and forum) for file attachments, automatically downloads them, and manages versions. It's perfect for server admins, mod developers, or anyone who needs to keep local files synced with Discord uploads.

## Key Features

- 🖥️ **Multi-Channel Support**: Monitor multiple text and forum channels simultaneously.
- 🔍 **File Type Filtering**: Customize which file types to download based on extensions.
- ⏱️ **Scheduled Updates**: Automatically check for new files at specified intervals.
- 🤖 **Discord Commands**: Manage the bot directly through Discord with easy-to-use commands.
- 📦 **Version Control**: Keep track of file versions with timestamp-based naming.
- 🔔 **Notification System**: Get notified in a specified Discord channel when new files are downloaded.
- 🔒 **Secure**: Uses environment variables for sensitive information.

## Technical Details

- Built with Python 3.7+
- Utilizes discord.py for Discord API interaction
- Asynchronous design for efficient performance
- Easy to set up and customize

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/discord-file-updater.git
   cd discord-file-updater
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables in a `.env` file:
   ```
   DISCORD_BOT_TOKEN=your_bot_token_here
   DISCORD_CHANNEL_IDS=channel_id1,channel_id2,channel_id3
   PLUGINS_DIR=/path/to/your/plugins/directory
   ALLOWED_EXTENSIONS=.zip,.jar
   UPDATE_INTERVAL=3600
   NOTIFICATION_CHANNEL_ID=notification_channel_id
   ```

4. Run the bot:
   ```
   python discord_file_updater.py
   ```

## Usage

- `!update`: Manually trigger an update check
- `!list_files`: List all files in the plugins directory
- `!add_channel <channel_id>`: Add a new channel to monitor
- `!remove_channel <channel_id>`: Remove a channel from monitoring

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
