# Tags

Tagging information related to this run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_anomaly_tag** | **bool** | Specifies whether the run has an anomaly tag. | [optional] 
**tags** | [**List[SnapshotTag]**](SnapshotTag.md) | Specifies the tags associated with the backup run. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.tags import Tags

# TODO update the JSON string below
json = "{}"
# create an instance of Tags from a JSON string
tags_instance = Tags.from_json(json)
# print the JSON string representation of the object
print(Tags.to_json())

# convert the object into a dict
tags_dict = tags_instance.to_dict()
# create an instance of Tags from a dict
tags_from_dict = Tags.from_dict(tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


