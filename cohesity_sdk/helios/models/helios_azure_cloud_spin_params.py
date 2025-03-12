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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class HeliosAzureCloudSpinParams(BaseModel):
    """
    Specifies various resources when converting and deploying a VM to Azure.
    """ # noqa: E501
    availability_set_id: Optional[StrictInt] = Field(default=None, description="Specifies the availability set.", alias="availabilitySetId")
    network_resource_group_id: Optional[StrictInt] = Field(default=None, description="Specifies id of the resource group for the selected virtual network.", alias="networkResourceGroupId")
    resource_group_id: Optional[StrictInt] = Field(default=None, description="Specifies id of the Azure resource group. Its value is globally unique within Azure.", alias="resourceGroupId")
    storage_account_id: Optional[StrictInt] = Field(default=None, description="Specifies id of the storage account that will contain the storage container within which we will create the blob that will become the VHD disk for the cloned VM.", alias="storageAccountId")
    storage_container_id: Optional[StrictInt] = Field(default=None, description="Specifies id of the storage container within the above storage account.", alias="storageContainerId")
    storage_resource_group_id: Optional[StrictInt] = Field(default=None, description="Specifies id of the resource group for the selected storage account.", alias="storageResourceGroupId")
    temp_vm_resource_group_id: Optional[StrictInt] = Field(default=None, description="Specifies id of the temporary Azure resource group.", alias="tempVmResourceGroupId")
    temp_vm_storage_account_id: Optional[StrictInt] = Field(default=None, description="Specifies id of the temporary VM storage account that will contain the storage container within which we will create the blob that will become the VHD disk for the cloned VM.", alias="tempVmStorageAccountId")
    temp_vm_storage_container_id: Optional[StrictInt] = Field(default=None, description="Specifies id of the temporary VM storage container within the above storage account.", alias="tempVmStorageContainerId")
    temp_vm_subnet_id: Optional[StrictInt] = Field(default=None, description="Specifies Id of the temporary VM subnet within the above virtual network.", alias="tempVmSubnetId")
    temp_vm_virtual_network_id: Optional[StrictInt] = Field(default=None, description="Specifies Id of the temporary VM Virtual Network.", alias="tempVmVirtualNetworkId")
    __properties: ClassVar[List[str]] = ["availabilitySetId", "networkResourceGroupId", "resourceGroupId", "storageAccountId", "storageContainerId", "storageResourceGroupId", "tempVmResourceGroupId", "tempVmStorageAccountId", "tempVmStorageContainerId", "tempVmSubnetId", "tempVmVirtualNetworkId"]

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
        """Create an instance of HeliosAzureCloudSpinParams from a JSON string"""
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
        # set to None if availability_set_id (nullable) is None
        # and model_fields_set contains the field
        if self.availability_set_id is None and "availability_set_id" in self.model_fields_set:
            _dict['availabilitySetId'] = None

        # set to None if network_resource_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.network_resource_group_id is None and "network_resource_group_id" in self.model_fields_set:
            _dict['networkResourceGroupId'] = None

        # set to None if resource_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.resource_group_id is None and "resource_group_id" in self.model_fields_set:
            _dict['resourceGroupId'] = None

        # set to None if storage_account_id (nullable) is None
        # and model_fields_set contains the field
        if self.storage_account_id is None and "storage_account_id" in self.model_fields_set:
            _dict['storageAccountId'] = None

        # set to None if storage_container_id (nullable) is None
        # and model_fields_set contains the field
        if self.storage_container_id is None and "storage_container_id" in self.model_fields_set:
            _dict['storageContainerId'] = None

        # set to None if storage_resource_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.storage_resource_group_id is None and "storage_resource_group_id" in self.model_fields_set:
            _dict['storageResourceGroupId'] = None

        # set to None if temp_vm_resource_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.temp_vm_resource_group_id is None and "temp_vm_resource_group_id" in self.model_fields_set:
            _dict['tempVmResourceGroupId'] = None

        # set to None if temp_vm_storage_account_id (nullable) is None
        # and model_fields_set contains the field
        if self.temp_vm_storage_account_id is None and "temp_vm_storage_account_id" in self.model_fields_set:
            _dict['tempVmStorageAccountId'] = None

        # set to None if temp_vm_storage_container_id (nullable) is None
        # and model_fields_set contains the field
        if self.temp_vm_storage_container_id is None and "temp_vm_storage_container_id" in self.model_fields_set:
            _dict['tempVmStorageContainerId'] = None

        # set to None if temp_vm_subnet_id (nullable) is None
        # and model_fields_set contains the field
        if self.temp_vm_subnet_id is None and "temp_vm_subnet_id" in self.model_fields_set:
            _dict['tempVmSubnetId'] = None

        # set to None if temp_vm_virtual_network_id (nullable) is None
        # and model_fields_set contains the field
        if self.temp_vm_virtual_network_id is None and "temp_vm_virtual_network_id" in self.model_fields_set:
            _dict['tempVmVirtualNetworkId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosAzureCloudSpinParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availabilitySetId": obj.get("availabilitySetId"),
            "networkResourceGroupId": obj.get("networkResourceGroupId"),
            "resourceGroupId": obj.get("resourceGroupId"),
            "storageAccountId": obj.get("storageAccountId"),
            "storageContainerId": obj.get("storageContainerId"),
            "storageResourceGroupId": obj.get("storageResourceGroupId"),
            "tempVmResourceGroupId": obj.get("tempVmResourceGroupId"),
            "tempVmStorageAccountId": obj.get("tempVmStorageAccountId"),
            "tempVmStorageContainerId": obj.get("tempVmStorageContainerId"),
            "tempVmSubnetId": obj.get("tempVmSubnetId"),
            "tempVmVirtualNetworkId": obj.get("tempVmVirtualNetworkId")
        })
        return _obj


