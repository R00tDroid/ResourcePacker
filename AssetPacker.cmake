set(asset_packer_directory ${CMAKE_CURRENT_LIST_DIR} CACHE STRING "")

function(pack_assets target sources output)
    set(AssetGenDir ${asset_packer_directory}/Generated)

    find_package(Python COMPONENTS Interpreter)

    add_custom_target(${target}_assets COMMAND "${Python_EXECUTABLE}" "${asset_packer_directory}/Source/AssetPack.py" "-output" "${output}" "--include" "${sources}")
    add_dependencies(${target} ${target}_assets)

    set(asset_files ${output}.cpp ${output}.hpp)
    set_source_files_properties(${asset_files} PROPERTIES GENERATED TRUE)
    target_sources(${target} PRIVATE ${asset_files})
endfunction()
