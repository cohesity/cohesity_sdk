# MongoDBCdpJobInfo

Specifies the CDP related information for a given MongoDB protection group. This will only be populated when the protection group is configured with a CDP policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest_recovery_point_in_time_usecs** | **int** | Specifies the latest available recovery point timestamp (in microseconds from epoch) | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mongo_db_cdp_job_info import MongoDBCdpJobInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDBCdpJobInfo from a JSON string
mongo_db_cdp_job_info_instance = MongoDBCdpJobInfo.from_json(json)
# print the JSON string representation of the object
print(MongoDBCdpJobInfo.to_json())

# convert the object into a dict
mongo_db_cdp_job_info_dict = mongo_db_cdp_job_info_instance.to_dict()
# create an instance of MongoDBCdpJobInfo from a dict
mongo_db_cdp_job_info_from_dict = MongoDBCdpJobInfo.from_dict(mongo_db_cdp_job_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


