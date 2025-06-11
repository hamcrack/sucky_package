# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_sucky_package_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED sucky_package_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(sucky_package_FOUND FALSE)
  elseif(NOT sucky_package_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(sucky_package_FOUND FALSE)
  endif()
  return()
endif()
set(_sucky_package_CONFIG_INCLUDED TRUE)

# output package information
if(NOT sucky_package_FIND_QUIETLY)
  message(STATUS "Found sucky_package: 0.0.0 (${sucky_package_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'sucky_package' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${sucky_package_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(sucky_package_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${sucky_package_DIR}/${_extra}")
endforeach()
