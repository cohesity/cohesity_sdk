# FailedRunDetails

Specifies a list of ids of Protection Group Runs that failed to update along with error details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Specifies the error mesage for failed run. | [optional] 
**run_id** | **str** | Specifies the id of the failed run. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.failed_run_details import FailedRunDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FailedRunDetails from a JSON string
failed_run_details_instance = FailedRunDetails.from_json(json)
# print the JSON string representation of the object
print(FailedRunDetails.to_json())

# convert the object into a dict
failed_run_details_dict = failed_run_details_instance.to_dict()
# create an instance of FailedRunDetails from a dict
failed_run_details_from_dict = FailedRunDetails.from_dict(failed_run_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


