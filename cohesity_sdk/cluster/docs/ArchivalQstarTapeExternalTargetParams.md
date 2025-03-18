# ArchivalQstarTapeExternalTargetParams

Specifies the parameters which are specific to QStar Tape related External Targets of archival purpose type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Specifies the host of the QStar Tape external target. | 
**integral_volume_names** | **List[str]** | Specifies the Integral Volume Names of the QStar Tape external target. | [optional] 
**is_forever_incremental_archival_enabled** | **bool** | Specifies if Forever Incremental Archival setting is enabled or not. | [optional] 
**is_incremental_archival_enabled** | **bool** | Specifies if Incremental Archival setting is enabled or not. | [optional] 
**password** | **str** | Specifies the Password of the QStar Tape external target. | [optional] 
**share_type** | **str** | Specifies the share type of QStar Tape external target. | [optional] 
**use_https** | **bool** | Specifies whether HTTPS is used or not. | [optional] 
**username** | **str** | Specifies the Username of the QStar Tape external target. | 
**web_services_port** | **int** | Specifies the Web Services Port of the QStar Tape external target. | 

## Example

```python
from cohesity_sdk.cluster.models.archival_qstar_tape_external_target_params import ArchivalQstarTapeExternalTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalQstarTapeExternalTargetParams from a JSON string
archival_qstar_tape_external_target_params_instance = ArchivalQstarTapeExternalTargetParams.from_json(json)
# print the JSON string representation of the object
print(ArchivalQstarTapeExternalTargetParams.to_json())

# convert the object into a dict
archival_qstar_tape_external_target_params_dict = archival_qstar_tape_external_target_params_instance.to_dict()
# create an instance of ArchivalQstarTapeExternalTargetParams from a dict
archival_qstar_tape_external_target_params_from_dict = ArchivalQstarTapeExternalTargetParams.from_dict(archival_qstar_tape_external_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


