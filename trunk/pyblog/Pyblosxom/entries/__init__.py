#######################################################################
# This file is part of PyBlosxom.
#
# Copyright (c) 2003, 2004, 2005, 2006 Wari Wahab
# 
# PyBlosxom is distributed under the MIT license.  See the file LICENSE
# for distribution details.
#
# $Id: __init__.py 913 2006-08-08 20:29:42Z willhelm $
#######################################################################
"""
PyBlosxom does most of its work on "entries".  Each entry is a single
unit of content which has a series of metadata properties (mtime, filename,
id, ...) and also a block of data content.  Entries can come from the
filesystem, SQL, or anywhere else.  They can be generated dynamically
or statically.

The purpose of an Entry object is to encapsulate the metadata and data 
of the entry for later filtering and rendering by the other components 
of Pyblosxom.
"""

__revision__ = "$Revision: 913 $"
