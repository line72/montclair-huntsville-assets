# -*- mode: python -*-

import transmogrifier

CONFIG = transmogrifier.Config(
    build_dir = './build',
    repo = 'huntsville',
    package_name = 'montclair-huntsville',
    name = 'Go Huntsville',
    description = 'Real Time Tracking of the Buses for Huntsville, AL',
    url = 'https://huntsville.gotransitapp.com',
    logo_svg = 'assets/logo.svg',
    montclair_config = transmogrifier.MontclairConfig(
        version = '1.4.2',
        revision = '2',
        title = 'Go Huntsville',
        first_run_text = "Welcome to Huntsville, AL's Real Time Bus Tracker.<br /><br />Please select one or more routes to begin!",
        configuration_js_file = 'assets/Configuration.js'
    ),
    ios_config = transmogrifier.MontclairiOSConfig(
        version = '2.0.4',
        revision = '1',
        app_id = 'com.gotransitapp.huntsville',
        app_store_id = '1494807745',
        app_store_url = 'https://apps.apple.com/us/app/go-huntsville/id1494807745'
    ),
    android_config = transmogrifier.MontclairAndroidConfig(
        version = '1.0.2',
        revision = '1',
        app_id = 'com.gotransitapp.huntsville',
        play_store_url = 'https://play.google.com/store/apps/details?id=com.gotransitapp.huntsville'
    )
)
