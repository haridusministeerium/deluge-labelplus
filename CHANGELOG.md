## 0.3.2.7 (unreleased)

- fix common/get_resource()
   - the initial fix introduced by #6 was insufficient. with that fix the
     client failed to start w/ following err:
     > (deluge:1): Gtk-ERROR **: 23:45:56.424: failed to add UI: Failed to open file “/home/user/.config/deluge/plugins/LabelPlus-0.3.2.6.egg/labelplus/data/blk_add_torrent_ext.ui”: Not a directory
   
     - pkg_resources.resource_filename() knew how to handle this. For a resource living inside a zip,
       it would silently extract it to a real temp cache directory (the old PYTHON_EGG_CACHE) and hand
       back a genuine filesystem path — something GTK's Gtk.Builder/add_from_file() could actually open().
     - importlib.resources.files(...) instead returns a Traversable. When the package lives inside a zip,
       that's effectively a zipfile.Path — it does not correspond to a real file on disk. Calling str()
       on it just concatenates path components, producing a string that looks like a normal filesystem
       path (.../AutoRemovePlus-0.6.9.egg/autoremoveplus/data/config.ui) but isn't one — the .egg segment
       is a zip file, not a directory, so nothing was ever extracted.
       GTK then tries to open that string with a plain filesystem call, hits the .egg component expecting
       a directory, finds a zip file instead, and libc returns ENOTDIR.
   - fix is to use importlib.resources.as_file(). however, something as
     simple as following doesn't work either:
       def get_resource(filename):
           ref = files("autoremoveplus").joinpath("data", filename)
           with as_file(ref) as path:
               return str(path)
       - this would cause client to err out w/ following, because as_file() only guarantees the extracted
         file exists while its with block is open:
         > failed to add UI: Failed to open file “/tmp/tmp91i1h82nconfig.ui”: No such file or directory
       - fix is to keep the extracted file alive using ExitStack
       - functools.lru_cache gives us the "extract once, reuse forever"

## 0.3.2.6 (2026-09-01)
- add mise.toml
- fix the pkg_resources deprecation (thanks @wendellavila !) -- #6
- migrate from drone to GH actions

## 0.3.2.5 (2022-10-30)
- Correct segmentation fault in Wayland

## 0.3.2.4 (2022-10-07)
- add zest.releaser
- add drone-ci integration

## 0.3.2.2
- Fix mapping without wildcard during config conversion

## 0.3.2.1
- Fix browse button exception when using remote clients

## 0.3.2.0
- Add autolabel criteria: label, filename
- Add option to move torrents to label specific download destination
- Add preference for resetting torrent options on label unset

## 0.3.1.0
- Add label assignment functionality to torrent context menu in WebUI
- Fix move on path changes not being activated for labels with no children

## 0.3.0.7
- Fix timestamp issue that caused label data to be constantly reloaded
- Fix removal of unlabeled torrent not being reflected in label tree

## 0.3.0.6
- Fix UI not being enabled in classic mode

## 0.3.0.5
- Fix drag-n-drop autoscroll stopping on selected label
- Fix drag-n-drop not disabling autoscroll/autoexpand on failed drop

## 0.3.0.4
- Fix preferences not loading when plugin first enabled

## 0.3.0.3
- Fix event deregister issue that conflicted with other plugins

## 0.3.0.2
- Remove misbehaving scroll to top hack

## 0.3.0.1
- Fix dialogs not closing when label is invalidated

## 0.3.0.0
- Autolabel now uses criteria based matching
- Test autolabel using a collapsible test area
- Select multiple label filters
- Move labels using the rename dialog or sidebar drag-n-drop
- Switch labels from within dialogs
- Toggle fullname in various places independently
- Label options added to torrent context menu
- Revert label options by page

- Dialogs are no longer modal
- Popup file chooser replaced with browse dialog
- Sidebar menu operates on right-clicked label without changing filter
- Sidebar menu no longer contains "All" options
- Status bar no longer opens label options
- Dependency on MoveTools removed

- Fix shared limit not updating when label added/removed

## 0.2.19.3
- Fix status bar not updating when label removed
- Improve performance when removing label with many sublabels
- Check for same path before attemping to move completed torrents

## 0.2.19.2
- Fix context menu using the wrong label when using "Parent"
- Allow "Parent" to be used by multiple selected torrents with the same label
- Re-add ability to jump to selected torrent's label
- Display base name in dialogs and full name in tooltips

## 0.2.19.1
- Fix label based subfolder appending full name when selected

## 0.2.19
- Set bandwidth limits per label
- Add label bandwidth usage to status bar
- Context menu navigation for less reliance on sidebar
- Some shortcuts to make navigating labels quicker
- Update config format to save sidebar state per daemon
- Increase compatibility with older versions of Gtk
- Various behavioral and cosmetic modifications

## 0.2.18
- Add auto-label regex support

## 0.2.17
- Add ability to jump to label in the sidebar based on a torrent's label
- Fix bug where only the first tracker was matched when autolabeling
- Fix bug where torrents set to no label were not moved back to default path

## 0.2.16
- Override Deluge 1.3.6 styling so that expanders are indented
- Various fixes

## 0.2.15
- Drag and drop torrents on label tree to label them
- Move label tree to its own tab for proper scrolling
- Move completed after recheck (if 'move on label path change' set in prefs)
- Various fixes

## 0.2.14
- Add auto move completed when label path changes (Requires Move Tools)
- Minor fixes

## 0.2.13
- Add label field to add torrent dialog
- Fix caching bug in torrent add/remove handlers

## 0.2.12
- Add client-side caching

## 0.2.11
- Add preference to toggle between short/full label names
