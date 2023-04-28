add_rules("mode.debug", "mode.release")

set_languages("c99", "c++17")

-- EasyX
package("easyx")
    set_description("easyx")
    
    on_load(function (package)
        package:set("installdir", path.join(os.scriptdir(), package:plat(), package:arch(), package:mode()))
    end)

    on_fetch(function (package) 
        local result = {}
        result.links = "EasyXa"
        result.linkdirs = package:installdir("lib")
        result.includedirs = package:installdir("include")
        return result
    end)
package_end()

-- Main Project: DaijinTheNeko
target("DaijinTheNeko")
    add_rules("win.sdk.mfc.static_app")
    set_kind("binary")
    add_includedirs("src")
    add_files("src/*.cpp")

    add_packages("easyx")
    add_linkdirs("easyx/lib") -- ??
    -- add_ldflags("/MDd")
target_end()


