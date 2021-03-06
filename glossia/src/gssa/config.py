# This file is part of the Go-Smart Simulation Architecture (GSSA).
# Go-Smart is an EU-FP7 project, funded by the European Commission.
#
# Copyright (C) 2013-  NUMA Engineering Ltd. (see AUTHORS file)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import gosmart_sf_config
import yaml
import logging

logger = logging.getLogger(__name__)

# CMake generated module
git_revision = gosmart_sf_config.git_revision
etc_location = gosmart_sf_config.etc_location

__config = None
__config_file = None
__api_version = 'A0.1'


def init_logger():
    """Set up logging.

    Uses standard Python logging module, although will set up
    ``txaio`` if ``logging.txaio`` is True in the configuration.

    """
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    if get('logging.txaio', False):
        import txaio
        txaio.start_logging()


def init_config(config_file=None):
    """Load the configuration file.

    Args:
        config_file (Optional[str]): Load the YAML configuration
            from this file. Defaults to [etc_location]/glossia.yml.
            In a system-wide install, this might be
            /usr/local/etc/glossia/glossia.yml

    """
    global __config, __config_file

    if config_file is None:
        config_file = os.path.join(etc_location, 'glossia.yml')

    __config_file = config_file

    try:
        with open(config_file, 'r') as config_fileh:
            __config = yaml.safe_load(config_fileh)
    except IOError:
        logger.warning("[no config file found]")
        __config = {}


def get(key, default=None):
    """Get a value from the global configuration.

    If the config file is not loaded, it will be loaded when this is
    called.

    Args:
        key (str): A dot-separated hierarchical key to find in the YAML
            configuration file.
        default (Optional) : Fall-back to return if the key is not found.
            Defaults to None.

    """
    if __config is None:
        init_config()

    try:
        value = __config
        for key_level in key.split('.'):
            value = value[key_level]
        return value
    except KeyError:
        return default


def get_config_file():
    """Get the location of the main configuration file."""
    return __config_file


def get_api_version():
    """Retrieve the API version for this server."""
    return __api_version
