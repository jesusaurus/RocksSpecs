# - Try to find SuiteSparse
# Once done this will define
#
#  SuiteSparse_FOUND        - system has SuiteSparse
#  SuiteSparse_INCLUDE_DIRS - include directories for SuiteSparse
#  SuiteSparse_LIBRARIES    - libraries for SuiteSparse

#=============================================================================
# Copyright (C) 2010 Anders Logg
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#=============================================================================

message(STATUS "Checking for package 'SuiteSparse'")

# Check for header file
find_path(SuiteSparse_INCLUDE_DIRS SuiteSparse_config.h
 HINTS ${SuiteSparse_DIR}/include $ENV{SuiteSparse_DIR}/include
 PATH_SUFFIXES suitesparse ufsparse
 DOC "Directory where the SuiteSparse header is located"
 )
mark_as_advanced(SuiteSparse_INCLUDE_DIRS)

# Check for SuiteSparse library
find_library(SuiteSparse_LIBRARIES suitesparseconfig
  HINTS ${SuiteSparse_DIR}/lib $ENV{SuiteSparse_DIR}/lib
  DOC "The SuiteSparse library"
  )
mark_as_advanced(SuiteSparse_LIBRARY)

# Standard package handling
include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(SuiteSparse
  "SuiteSparse could not be found. Be sure to set SuiteSparse_DIR."
  SuiteSparse_LIBRARIES SuiteSparse_INCLUDE_DIRS)
