# ListTrustedCasResult

Specifies the basic info about CA Root Certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | [**List[TrustedCa]**](TrustedCa.md) | Array of trusted certificates. Specifies the list of certificates returned in this response. List is not sorted. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.list_trusted_cas_result import ListTrustedCasResult

# TODO update the JSON string below
json = "{}"
# create an instance of ListTrustedCasResult from a JSON string
list_trusted_cas_result_instance = ListTrustedCasResult.from_json(json)
# print the JSON string representation of the object
print(ListTrustedCasResult.to_json())

# convert the object into a dict
list_trusted_cas_result_dict = list_trusted_cas_result_instance.to_dict()
# create an instance of ListTrustedCasResult from a dict
list_trusted_cas_result_from_dict = ListTrustedCasResult.from_dict(list_trusted_cas_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


