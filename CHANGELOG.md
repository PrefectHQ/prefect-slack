# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

- Updated branding

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security


## 0.2.2

## 0.1.2

Released on January 31st, 2023.

### Fixed

- Renamed `prefect_slack.SlackWebhook._block_type_name` to prevent conflict with `prefect.SlackWebhook` - [#45](https://github.com/PrefectHQ/prefect-slack/pull/45)

## 0.1.1

Released on December 27th, 2022.

### Changed

- Converted `SlackCredentials` and `SlackWebhook` into a `Block` - [#29](https://github.com/PrefectHQ/prefect-slack/pull/29)

### Fixed

- The setup entrypoint to register blocks - [#40](https://github.com/PrefectHQ/prefect-slack/pull/40)

## 0.1.0

Released on March 7th, 2022.

### Added

- `send_chat_message` task - [#3](https://github.com/PrefectHQ/prefect-slack/pull/3)
- `send_incoming_webhook` task - [#5](https://github.com/PrefectHQ/prefect-slack/pull/5)
