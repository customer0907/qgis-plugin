# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PrintHelloWorld
                                 A QGIS plugin
 Plugin that print hello world
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-10-11
        copyright            : (C) 2024 by Changhee Lee
        email                : slajflzj12@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PrintHelloWorld class from file PrintHelloWorld.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Hello_World import PrintHelloWorld
    return PrintHelloWorld(iface)
