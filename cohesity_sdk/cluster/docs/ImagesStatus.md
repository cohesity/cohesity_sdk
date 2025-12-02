# ImagesStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_uid** | **int** | AppUid | [optional] 
**image_name** | **str** | Name of Image | [optional] 
**image_tags** | **List[str]** | Image tags available in registry | [optional] 
**loaded_images** | **List[str]** | Loaded Images | [optional] 
**status** | **str** | Image status | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.images_status import ImagesStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesStatus from a JSON string
images_status_instance = ImagesStatus.from_json(json)
# print the JSON string representation of the object
print(ImagesStatus.to_json())

# convert the object into a dict
images_status_dict = images_status_instance.to_dict()
# create an instance of ImagesStatus from a dict
images_status_from_dict = ImagesStatus.from_dict(images_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


