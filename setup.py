#
# setup.py
#
# Copyright (C) 2014 Ratanak Lun <ratanakvlun@gmail.com>
# Copyright (C) 2008 Martijn Voncken <mvoncken@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.    If not, write to:
# 	The Free Software Foundation, Inc.,
# 	51 Franklin Street, Fifth Floor
# 	Boston, MA  02110-1301, USA.
#
#    In addition, as a special exception, the copyright holders give
#    permission to link the code of portions of this program with the OpenSSL
#    library.
#    You must obey the GNU General Public License in all respects for all of
#    the code used other than OpenSSL. If you modify file(s) with this
#    exception, you may extend this exception to your version of the file(s),
#    but you are not obligated to do so. If you do not wish to do so, delete
#    this exception statement from your version. If you delete this exception
#    statement from all source files in the program, then also delete it here.
#

from setuptools import setup, find_packages
import os
import glob

# note the version is managed by zest.releaser:
version = "0.3.2.8.dev0"

__plugin_name__ = "LabelPlus"
__author__ = "Laur"
__url__ = "https://github.com/haridusministeerium/deluge-labelplus"
__license__ = "GPLv3"
__description__ = "Assign labels to torrents"
__long_description__ = """
Assign labels to torrents

Based on Label 0.2
by Martijn Voncken"""
__pkg_data__ = {__plugin_name__.lower():["template/*", "data/*"]}

setup(
    name=__plugin_name__,
    version=version,
    description=__description__,
    author=__author__,
    url=__url__,
    license=__license__,
    long_description=__long_description__,

    packages=find_packages(),
    package_data = __pkg_data__,
    python_requires='>=3.7',

    entry_points="""
    [deluge.plugin.core]
    %s = %s:CorePlugin
    [deluge.plugin.gtk3ui]
    %s = %s:Gtk3UIPlugin
    [deluge.plugin.web]
    %s = %s:WebUIPlugin
    """ % ((__plugin_name__, __plugin_name__.lower())*3)
)

# original setup-generated filename: LabelPlus-0.3.2.4-py3.9.egg

# rename generated.egg to exclude the py version from filename:
list_of_eggs = glob.glob('./dist/*.egg')
if list_of_eggs:
    newest_egg = max(list_of_eggs, key=os.path.getmtime)

    os.rename(
        newest_egg,
        os.path.join('dist', __plugin_name__ + '-' + version + '.egg')
    )
