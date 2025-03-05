# DataLockConstraints

Specifies the dataLock constraints for local or target snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_time_usecs** | **int** | Specifies the expiry time of attempt in Unix epoch Timestamp (in microseconds). | [optional] 
**mode** | **str** | Specifies the type of WORM retention type. &lt;br&gt;&#39;Compliance&#39; implies WORM retention is set for compliance reason. &lt;br&gt;&#39;Administrative&#39; implies WORM retention is set for administrative purposes. | [optional] 

## Example

```python
from cohesity_sdk.models.data_lock_constraints import DataLockConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of DataLockConstraints from a JSON string
data_lock_constraints_instance = DataLockConstraints.from_json(json)
# print the JSON string representation of the object
print(DataLockConstraints.to_json())

# convert the object into a dict
data_lock_constraints_dict = data_lock_constraints_instance.to_dict()
# create an instance of DataLockConstraints from a dict
data_lock_constraints_from_dict = DataLockConstraints.from_dict(data_lock_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


