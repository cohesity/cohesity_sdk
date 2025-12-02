# RecoverSapHanaParams

Specifies the parameters to recover SAP HANA objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional] [default to 1]
**recover_to** | **int** | Specifies the &#39;Source Registration ID&#39; of the source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**snapshots** | [**List[RecoverUdaSnapshotParams]**](RecoverUdaSnapshotParams.md) | Specifies the local snapshot ids and other details of the objects to be recovered. | 
**start_database** | **bool** | Start the database after the recovery is complete. | [optional] [default to True]
**warnings** | **List[str]** | This field will hold the warnings in cases where the job status is SucceededWithWarnings. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.recover_sap_hana_params import RecoverSapHanaParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverSapHanaParams from a JSON string
recover_sap_hana_params_instance = RecoverSapHanaParams.from_json(json)
# print the JSON string representation of the object
print(RecoverSapHanaParams.to_json())

# convert the object into a dict
recover_sap_hana_params_dict = recover_sap_hana_params_instance.to_dict()
# create an instance of RecoverSapHanaParams from a dict
recover_sap_hana_params_from_dict = RecoverSapHanaParams.from_dict(recover_sap_hana_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


