# SearchSfdcRecordsRequestParams

Specifies the parameters which are specific for searching Salesforce records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mutation_types** | **List[str]** | Specifies a list of mutuation types for an object. | 
**object_name** | **str** | Specifies the name of the object. | 
**query_string** | **str** | Specifies the query string to search records. Query string can be one or multiples clauses joined together by &#39;AND&#39; or &#39;OR&#39; claused. | [optional] 
**snapshot_id** | **str** | Specifies the id of the snapshot for the object. | 

## Example

```python
from cohesity_sdk.models.search_sfdc_records_request_params import SearchSfdcRecordsRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchSfdcRecordsRequestParams from a JSON string
search_sfdc_records_request_params_instance = SearchSfdcRecordsRequestParams.from_json(json)
# print the JSON string representation of the object
print(SearchSfdcRecordsRequestParams.to_json())

# convert the object into a dict
search_sfdc_records_request_params_dict = search_sfdc_records_request_params_instance.to_dict()
# create an instance of SearchSfdcRecordsRequestParams from a dict
search_sfdc_records_request_params_from_dict = SearchSfdcRecordsRequestParams.from_dict(search_sfdc_records_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


