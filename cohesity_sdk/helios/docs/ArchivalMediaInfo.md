# ArchivalMediaInfo

Specifies the media information in QStar Archival.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** | Specifies a unique identifier for the media. | [optional] [readonly] 
**is_online** | **bool** | Specifies a flag that indicates if the media is online or offline. Offline media must be manually loaded into the media library before a recovery can occur. | [optional] 
**location** | **str** | Specifies the location of the offline media as recorded by the backup administrator using media management software. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.archival_media_info import ArchivalMediaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalMediaInfo from a JSON string
archival_media_info_instance = ArchivalMediaInfo.from_json(json)
# print the JSON string representation of the object
print(ArchivalMediaInfo.to_json())

# convert the object into a dict
archival_media_info_dict = archival_media_info_instance.to_dict()
# create an instance of ArchivalMediaInfo from a dict
archival_media_info_from_dict = ArchivalMediaInfo.from_dict(archival_media_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


