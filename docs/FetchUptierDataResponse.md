# FetchUptierDataResponse

Specifies the amount of data in bytes estimated to be uptiered as part of the current restore job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_size** | **int** | Specifies the amount of data in bytes estimated to be uptiered as part of the current restore job. | [optional] 

## Example

```python
from cohesity_sdk.models.fetch_uptier_data_response import FetchUptierDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FetchUptierDataResponse from a JSON string
fetch_uptier_data_response_instance = FetchUptierDataResponse.from_json(json)
# print the JSON string representation of the object
print(FetchUptierDataResponse.to_json())

# convert the object into a dict
fetch_uptier_data_response_dict = fetch_uptier_data_response_instance.to_dict()
# create an instance of FetchUptierDataResponse from a dict
fetch_uptier_data_response_from_dict = FetchUptierDataResponse.from_dict(fetch_uptier_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


