# PauseMetadata

Encapsulation of all pause related data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_pause_modification_time_usecs** | **int** | Time in usec when the job was last paused or unpaused. | [optional] 
**last_paused_by_username** | **str** | The user who last paused this protection group. | [optional] 
**paused_note** | **str** | A note from the user explaining the reason for pausing future runs, if applicable. | [optional] 
**user_initiated_pause_requested_time_usecs** | **int** | Time in usec when user initiates protection run pause. This field gets populated on user initiated pause and gets cleared on user initiated resume. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.pause_metadata import PauseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PauseMetadata from a JSON string
pause_metadata_instance = PauseMetadata.from_json(json)
# print the JSON string representation of the object
print(PauseMetadata.to_json())

# convert the object into a dict
pause_metadata_dict = pause_metadata_instance.to_dict()
# create an instance of PauseMetadata from a dict
pause_metadata_from_dict = PauseMetadata.from_dict(pause_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


