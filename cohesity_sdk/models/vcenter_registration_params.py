# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.models.datastore_params import DatastoreParams
from cohesity_sdk.models.vmware_throttling_params import VmwareThrottlingParams
from typing import Optional, Set
from typing_extensions import Self

class VcenterRegistrationParams(BaseModel):
    """
    Specifies parameters to register VMware vCenter.
    """ # noqa: E501
    password: StrictStr = Field(description="Specifies the password to access target entity.")
    username: StrictStr = Field(description="Specifies the username to access target entity.")
    description: Optional[StrictStr] = Field(default=None, description="Specifies the description of the source being registered.")
    endpoint: StrictStr = Field(description="Specifies the endpoint IPaddress, URL or hostname of the host.")
    ca_cert: Optional[StrictStr] = Field(default=None, description="Specifies the CA certificate to enable SSL communication between host and cluster.", alias="caCert")
    data_store_params: Optional[List[DatastoreParams]] = Field(default=None, description="Specifies datastore specific parameters.", alias="dataStoreParams")
    link_vms_across_vcenter: Optional[StrictBool] = Field(default=None, description="Specifies if the VM linking feature is enabled for the VCenter. If enabled, migrated VMs present in the VCenter which earlier belonged to some other VCenter will be linked during EH refresh.", alias="linkVmsAcrossVcenter")
    min_free_datastore_space_for_backup_gb: Optional[StrictInt] = Field(default=None, description="Specifies the minimum free space (in GB) expected to be available in the datastore where the virtual disks of the VM being backed up reside. If the space available is lower than the specified value, backup will be aborted.", alias="minFreeDatastoreSpaceForBackupGb")
    min_free_datastore_space_for_backup_percentage: Optional[StrictInt] = Field(default=None, description="Specifies the minimum free space (in percentage) expected to be available in the datastore where the virtual disks of the VM being backed up reside. If the space available is lower than the specified value, backup will be aborted.", alias="minFreeDatastoreSpaceForBackupPercentage")
    throttling_params: Optional[VmwareThrottlingParams] = Field(default=None, alias="throttlingParams")
    use_vm_bios_uuid: Optional[StrictBool] = Field(default=None, description="Specifies to use VM BIOS UUID to track virtual machines in the host.", alias="useVmBiosUuid")
    __properties: ClassVar[List[str]] = ["password", "username", "description", "endpoint", "caCert", "dataStoreParams", "linkVmsAcrossVcenter", "minFreeDatastoreSpaceForBackupGb", "minFreeDatastoreSpaceForBackupPercentage", "throttlingParams", "useVmBiosUuid"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of VcenterRegistrationParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in data_store_params (list)
        _items = []
        if self.data_store_params:
            for _item_data_store_params in self.data_store_params:
                if _item_data_store_params:
                    _items.append(_item_data_store_params.to_dict())
            _dict['dataStoreParams'] = _items
        # override the default output from pydantic by calling `to_dict()` of throttling_params
        if self.throttling_params:
            _dict['throttlingParams'] = self.throttling_params.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if ca_cert (nullable) is None
        # and model_fields_set contains the field
        if self.ca_cert is None and "ca_cert" in self.model_fields_set:
            _dict['caCert'] = None

        # set to None if data_store_params (nullable) is None
        # and model_fields_set contains the field
        if self.data_store_params is None and "data_store_params" in self.model_fields_set:
            _dict['dataStoreParams'] = None

        # set to None if link_vms_across_vcenter (nullable) is None
        # and model_fields_set contains the field
        if self.link_vms_across_vcenter is None and "link_vms_across_vcenter" in self.model_fields_set:
            _dict['linkVmsAcrossVcenter'] = None

        # set to None if min_free_datastore_space_for_backup_gb (nullable) is None
        # and model_fields_set contains the field
        if self.min_free_datastore_space_for_backup_gb is None and "min_free_datastore_space_for_backup_gb" in self.model_fields_set:
            _dict['minFreeDatastoreSpaceForBackupGb'] = None

        # set to None if min_free_datastore_space_for_backup_percentage (nullable) is None
        # and model_fields_set contains the field
        if self.min_free_datastore_space_for_backup_percentage is None and "min_free_datastore_space_for_backup_percentage" in self.model_fields_set:
            _dict['minFreeDatastoreSpaceForBackupPercentage'] = None

        # set to None if use_vm_bios_uuid (nullable) is None
        # and model_fields_set contains the field
        if self.use_vm_bios_uuid is None and "use_vm_bios_uuid" in self.model_fields_set:
            _dict['useVmBiosUuid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VcenterRegistrationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "password": obj.get("password"),
            "username": obj.get("username"),
            "description": obj.get("description"),
            "endpoint": obj.get("endpoint"),
            "caCert": obj.get("caCert"),
            "dataStoreParams": [DatastoreParams.from_dict(_item) for _item in obj["dataStoreParams"]] if obj.get("dataStoreParams") is not None else None,
            "linkVmsAcrossVcenter": obj.get("linkVmsAcrossVcenter"),
            "minFreeDatastoreSpaceForBackupGb": obj.get("minFreeDatastoreSpaceForBackupGb"),
            "minFreeDatastoreSpaceForBackupPercentage": obj.get("minFreeDatastoreSpaceForBackupPercentage"),
            "throttlingParams": VmwareThrottlingParams.from_dict(obj["throttlingParams"]) if obj.get("throttlingParams") is not None else None,
            "useVmBiosUuid": obj.get("useVmBiosUuid")
        })
        return _obj


