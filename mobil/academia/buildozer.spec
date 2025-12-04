[app]

# (str) Title of your application
title = Academia

# (str) Package name
package.name = academia

# (str) Package domain (needed for android/ios packaging)
package.domain = org.academia.app

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
requirements = 
    python3==3.10.12,
    kivy==2.2.1,
    kivymd==1.1.1,
    pillow==10.0.1

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# Supported orientations (portrait or landscape)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color
# android.presplash_color = #FFFFFF

# (str) Adaptive icon of the application
# icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
# icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
android.permissions = 
    INTERNET,
    WRITE_EXTERNAL_STORAGE,
    READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use
android.ndk_api = 21

# (bool) Use private data storage
android.private_storage = True

# (list) Android archs to build for
# Recomendo usar apenas uma para builds de debug mais rápido
# android.archs = arm64-v8a
android.archs = armeabi-v7a

# (bool) Skip Android SDK update (mais rápido)
android.skip_update = False

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme
android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
# android.whitelist =

# (str) Path to a custom whitelist file
# android.whitelist_src =

# (list) Java .jar files to add
# android.add_jars =

# (list) Java files to add to the android project
# android.add_src =

# (list) Android AAR archives to add
# android.add_aars =

# (list) Gradle dependencies to add
# android.gradle_dependencies =

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Indicate whether the screen should stay on
# android.wakelock = False

# (list) Android application meta-data to set
# android.meta_data =

# (bool) enables Android auto backup feature
android.allow_backup = True

# (str) Android logcat filters (IMPORTANTE para debug)
android.logcat_filters = *:S python:D kivy:D MainThread:D

# (bool) Android logcat only display log for activity's pid
android.logcat_pid_only = False

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (int) overrides automatic versionCode computation
# android.numeric_version = 1

# (bool) Skip byte compile for .py files
# android.no-byte-compile-python = False

# (str) The format for debug mode
android.debug_artifact = apk

#
# Python for android (p4a) specific
#

# (str) python-for-android branch to use
p4a.branch = master

# (str) Bootstrap to use for android builds
p4a.bootstrap = sdl2

# Control passing the --use-setup-py vs --ignore-setup-py to p4a
# p4a.setup_py = false

# (str) extra command line arguments to pass when invoking pythonforandroid.toolchain
p4a.extra_args = --debug

# (list) add java compile options
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

#
# iOS specific (não necessário para Android)
#

#
# Buildozer settings
#

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

# (str) Path to build artifact storage
# build_dir = ./.buildozer

# (str) Path to build output storage
# bin_dir = ./bin

#
#    Profiles
#

#    -----------------------------------------------------------------------------
#    List as sections
#

#    (list) List of library references
# android.library_references =

#    (list) List of shared libraries
# android.uses_library =

#    (str) launchMode to set for the main activity
# android.manifest.launch_mode = standard

#    (list) Custom XML for AndroidManifest.xml
# android.extra_manifest_xml =

#    (list) Custom arguments for AndroidManifest.xml
# android.extra_manifest_application_arguments =

#    (list) Additional assets to include
# android.add_assets =

#    (list) Additional resources to include
# android.add_resources =

#    (list) Additional activities to include
# android.add_activities =

#    (str) OUYA Console category
# android.ouya.category = GAME

#    (str) Filename of OUYA Console icon
# android.ouya.icon.filename =

#    (str) XML file to include as intent filters
# android.manifest.intent_filters =

#    (list) Copy these files to src/main/res/xml/
# android.res_xml =

#    (str) screenOrientation to set
# android.manifest.orientation = portrait

#    (list) Android additional libraries to copy
# android.add_libs_armeabi =
# android.add_libs_armeabi_v7a =
# android.add_libs_arm64_v8a =
# android.add_libs_x86 =
# android.add_libs_mips =

#    (list) Gradle repositories to add
# android.add_gradle_repositories =

#    (list) packaging options to add
# android.add_packaging_options =

#    (str) The format for release mode
# android.release_artifact = aab
