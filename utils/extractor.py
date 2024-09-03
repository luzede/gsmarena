"""Extracting wanted data from a **BeautifulSoup** object."""

import re

from bs4 import BeautifulSoup

from utils.classes import DeviceDetails, DeviceSpecs


def device_details(document: BeautifulSoup) -> DeviceDetails:
    """Extract the device details from the header content of the device page

    Args:
        document (BeautifulSoup): The **BeautifulSoup** object of the device page

    Returns:
        DeviceDetailsShort: A dataclass containing the header content of the device page
    """
    model_name = document.find(
        "h1", attrs={"class": "specs-phone-name-title", "data-spec": "modelname"}
    )
    img_link = document.find("div", class_="specs-photo-main").find("img")
    released = document.find("span", attrs={"data-spec": "released-hl"})
    body = document.find("span", attrs={"data-spec": "body-hl"})
    os = document.find("span", attrs={"data-spec": "os-hl"})
    storage = document.find("span", attrs={"data-spec": "storage-hl"})
    display_size = document.find("span", attrs={"data-spec": "displaysize-hl"})
    display_res = document.find("span", attrs={"data-spec": "displayres-hl"})
    camera_pixels = document.find("span", attrs={"data-spec": "camerapixels-hl"})
    camera_pixel_unit = camera_pixels.find_next_sibling("span")
    video_pixels = document.find("span", attrs={"data-spec": "videopixels-hl"})
    ram_size = document.find("span", attrs={"data-spec": "ramsize-hl"})
    ram_size_unit = ram_size.find_next_sibling("span")
    chipset = document.find("span", attrs={"data-spec": "chipset-hl"})
    battery_size = document.find("span", attrs={"data-spec": "batsize-hl"})
    battery_size_unit = battery_size.find_next_sibling("span")
    battery_type = document.find("span", attrs={"data-spec": "battype-hl"})

    return DeviceDetails(
        model_name=model_name.text,
        img_link=img_link.get("src", None) if img_link else None,
        released=released.text,
        body=body.text if body else None,
        os=os.text if os else None,
        storage=storage.text if storage else None,
        display_size=display_size.text if display_size else None,
        display_res=display_res.text if display_res else None,
        camera_pixels=camera_pixels.text if camera_pixels else None,
        camera_pixel_unit=camera_pixel_unit.text if camera_pixel_unit else None,
        video_pixels=video_pixels.text if video_pixels else None,
        ram_size=ram_size.text if ram_size else None,
        ram_size_unit=ram_size_unit.text if ram_size_unit else None,
        chipset=chipset.text if chipset else None,
        battery_size=battery_size.text if battery_size else None,
        battery_size_unit=battery_size_unit.text if battery_size_unit else None,
        battery_type=battery_type.text if battery_type else None,
    )


def device_specs(document: BeautifulSoup) -> DeviceSpecs:
    """_summary_

    Args:
        document (BeautifulSoup): **gsmarena** device page

    Returns:
        DeviceSpecs: dataclass containing the device specs
    """
    specs_list = document.find("div", id="specs-list")

    model_name = specs_list.find("h1", attrs={"data-spec": "modelname"})
    img_link = specs_list.find("div", class_="specs-photo-main").find("img")

    comment = specs_list.find("p", attrs={"data-spec": "comment"})

    network_technology = specs_list.find("a", attrs={"data-spec": "nettech"})
    network_speed = specs_list.find("td", attrs={"data-spec": "speed"})

    launch_announced = specs_list.find("td", attrs={"data-spec": "year"})
    launch_status = specs_list.find("td", attrs={"data-spec": "status"})

    body_dimensions = specs_list.find("td", attrs={"data-spec": "dimensions"})
    body_weight = specs_list.find("td", attrs={"data-spec": "weight"})
    body_build = specs_list.find("td", attrs={"data-spec": "build"})
    body_sim = specs_list.find(
        "td", attrs={"data-spec": "sim"}
    )  # it has <br> inside, need to extract in a way that can be handled later on
    body_other = specs_list.find(
        "td", attrs={"data-spec": "bodyother"}
    )  # also has <br> inside separating the data

    display_type = specs_list.find("td", attrs={"data-spec": "displaytype"})
    display_size = specs_list.find(
        "td", attrs={"data-spec": "displaysize"}
    )  # it might have <sup> inside
    display_resolution = specs_list.find("td", attrs={"data-spec": "displayresolution"})
    display_protection = specs_list.find("td", attrs={"data-spec": "displayprotection"})
    display_other = specs_list.find("td", attrs={"data-spec": "displayother"})

    platform_os = specs_list.find("td", attrs={"data-spec": "os"})
    platform_chipset = specs_list.find("td", attrs={"data-spec": "chipset"})
    platform_cpu = specs_list.find("td", attrs={"data-spec": "cpu"})
    platform_gpu = specs_list.find("td", attrs={"data-spec": "gpu"})

    memory_card_slot = specs_list.find("td", attrs={"data-spec": "memoryslot"})
    memory_internal = specs_list.find("td", attrs={"data-spec": "internalmemory"})
    memory_other = specs_list.find("td", attrs={"data-spec": "memoryother"})

    main_camera_type = specs_list.find(
        "a",
        string=re.compile(r"Single|Dual|Triple|Quad"),
        href="glossary.php3?term=camera",
    )
    main_camera_specs = specs_list.find(
        "td", attrs={"data-spec": "cam1modules"}
    )  # It might have <br> inside,
    main_camera_features = specs_list.find("td", attrs={"data-spec": "cam1features"})
    main_camera_video = specs_list.find("td", attrs={"data-spec": "cam1video"})

    selfie_camera_type = specs_list.find(
        "a",
        string=re.compile(r"Single|Dual|Triple|Quad"),
        href="glossary.php3?term=secondary-camera",
    )
    selfie_camera_specs = specs_list.find(
        "td", attrs={"data-spec": "cam2modules"}
    )  # It might have <br> inside
    selfie_camera_features = specs_list.find("td", attrs={"data-spec": "cam2features"})
    selfie_camera_video = specs_list.find("td", attrs={"data-spec": "cam2video"})

    comms_wlan = specs_list.find("td", attrs={"data-spec": "wlan"})
    comms_bluetooth = specs_list.find("td", attrs={"data-spec": "bluetooth"})
    comms_gps = specs_list.find("td", attrs={"data-spec": "gps"})
    comms_nfc = specs_list.find("td", attrs={"data-spec": "nfc"})
    comms_radio = specs_list.find("td", attrs={"data-spec": "radio"})
    comms_usb = specs_list.find("td", attrs={"data-spec": "usb"})

    features_sensors = specs_list.find("td", attrs={"data-spec": "sensors"})
    features_other = specs_list.find("td", attrs={"data-spec": "featuresother"})

    battery_type = specs_list.find("td", attrs={"data-spec": "batdescription1"})

    misc_colors = specs_list.find("td", attrs={"data-spec": "colors"})
    misc_models = specs_list.find("td", attrs={"data-spec": "models"})
    misc_price = specs_list.find("td", attrs={"data-spec": "price"})

    return DeviceSpecs(
        model_name=model_name.text,
        img_link=img_link.get("src", None) if img_link else None,
        comment=comment.text if comment else None,
        network_technology=network_technology.text if network_technology else None,
        network_speed=network_speed.text if network_speed else None,
        launch_announced=launch_announced.text if launch_announced else None,
        launch_status=launch_status.text if launch_status else None,
        body_dimensions=body_dimensions.text if body_dimensions else None,
        body_weight=body_weight.text if body_weight else None,
        body_build=body_build.text if body_build else None,
        body_sim=body_sim.text if body_sim else None,
        body_other=body_other.text if body_other else None,
        display_type=display_type.text if display_type else None,
        display_size=display_size.text if display_size else None,
        display_resolution=display_resolution.text if display_resolution else None,
        display_protection=display_protection.text if display_protection else None,
        display_other=display_other.text if display_other else None,
        platform_os=platform_os.text if platform_os else None,
        platform_chipset=platform_chipset.text if platform_chipset else None,
        platform_cpu=platform_cpu.text if platform_cpu else None,
        platform_gpu=platform_gpu.text if platform_gpu else None,
        memory_card_slot=memory_card_slot.text if memory_card_slot else None,
        memory_internal=memory_internal.text if memory_internal else None,
        memory_other=memory_other.text if memory_other else None,
        main_camera_type=main_camera_type.text if main_camera_type else None,
        main_camera_specs=main_camera_specs.text if main_camera_specs else None,
        main_camera_features=main_camera_features.text
        if main_camera_features
        else None,
        main_camera_video=main_camera_video.text if main_camera_video else None,
        selfie_camera_type=selfie_camera_type.text if selfie_camera_type else None,
        selfie_camera_specs=selfie_camera_specs.text if selfie_camera_specs else None,
        selfie_camera_features=selfie_camera_features.text
        if selfie_camera_features
        else None,
        selfie_camera_video=selfie_camera_video.text if selfie_camera_video else None,
        comms_wlan=comms_wlan.text if comms_wlan else None,
        comms_bluetooth=comms_bluetooth.text if comms_bluetooth else None,
        comms_gps=comms_gps.text if comms_gps else None,
        comms_nfc=comms_nfc.text if comms_nfc else None,
        comms_radio=comms_radio.text if comms_radio else None,
        comms_usb=comms_usb.text if comms_usb else None,
        features_sensors=features_sensors.text if features_sensors else None,
        features_other=features_other.text if features_other else None,
        battery_type=battery_type.text if battery_type else None,
        misc_colors=misc_colors.text if misc_colors else None,
        misc_models=misc_models.text if misc_models else None,
        misc_price=misc_price.text if misc_price else None,
    )
