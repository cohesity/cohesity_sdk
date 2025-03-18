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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class HeliosAzureTargetConfig(BaseModel):
    """
    Specifies the configuration for adding Azure as replication target
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the Azure Replication target.")
    resource_group: Optional[StrictInt] = Field(default=None, description="Specifies id of the Azure resource group used to filter regions in UI.", alias="resourceGroup")
    resource_group_name: Optional[StrictStr] = Field(default=None, description="Specifies name of the Azure resource group used to filter regions in UI.", alias="resourceGroupName")
    source_id: Optional[StrictInt] = Field(description="Specifies the source id of the Azure protection source registered on Cohesity cluster.", alias="sourceId")
    storage_account: Optional[StrictInt] = Field(default=None, description="Specifies id of the storage account of Azure replication target which will contain storage container.", alias="storageAccount")
    storage_account_name: Optional[StrictStr] = Field(default=None, description="Specifies name of the storage account of Azure replication target which will contain storage container.", alias="storageAccountName")
    storage_container: Optional[StrictInt] = Field(default=None, description="Specifies id of the storage container of Azure Replication target.", alias="storageContainer")
    storage_container_name: Optional[StrictStr] = Field(default=None, description="Specifies name of the storage container of Azure Replication target.", alias="storageContainerName")
    storage_resource_group: Optional[StrictInt] = Field(default=None, description="Specifies id of the storage resource group of Azure Replication target.", alias="storageResourceGroup")
    storage_resource_group_name: Optional[StrictStr] = Field(default=None, description="Specifies name of the storage resource group of Azure Replication target.", alias="storageResourceGroupName")
    __properties: ClassVar[List[str]] = ["name", "resourceGroup", "resourceGroupName", "sourceId", "storageAccount", "storageAccountName", "storageContainer", "storageContainerName", "storageResourceGroup", "storageResourceGroupName"]

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
        """Create an instance of HeliosAzureTargetConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "name",
            "resource_group_name",
            "storage_account",
            "storage_account_name",
            "storage_container",
            "storage_container_name",
            "storage_resource_group",
            "storage_resource_group_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if resource_group (nullable) is None
        # and model_fields_set contains the field
        if self.resource_group is None and "resource_group" in self.model_fields_set:
            _dict['resourceGroup'] = None

        # set to None if resource_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.resource_group_name is None and "resource_group_name" in self.model_fields_set:
            _dict['resourceGroupName'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        # set to None if storage_account (nullable) is None
        # and model_fields_set contains the field
        if self.storage_account is None and "storage_account" in self.model_fields_set:
            _dict['storageAccount'] = None

        # set to None if storage_account_name (nullable) is None
        # and model_fields_set contains the field
        if self.storage_account_name is None and "storage_account_name" in self.model_fields_set:
            _dict['storageAccountName'] = None

        # set to None if storage_container (nullable) is None
        # and model_fields_set contains the field
        if self.storage_container is None and "storage_container" in self.model_fields_set:
            _dict['storageContainer'] = None

        # set to None if storage_container_name (nullable) is None
        # and model_fields_set contains the field
        if self.storage_container_name is None and "storage_container_name" in self.model_fields_set:
            _dict['storageContainerName'] = None

        # set to None if storage_resource_group (nullable) is None
        # and model_fields_set contains the field
        if self.storage_resource_group is None and "storage_resource_group" in self.model_fields_set:
            _dict['storageResourceGroup'] = None

        # set to None if storage_resource_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.storage_resource_group_name is None and "storage_resource_group_name" in self.model_fields_set:
            _dict['storageResourceGroupName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosAzureTargetConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "resourceGroup": obj.get("resourceGroup"),
            "resourceGroupName": obj.get("resourceGroupName"),
            "sourceId": obj.get("sourceId"),
            "storageAccount": obj.get("storageAccount"),
            "storageAccountName": obj.get("storageAccountName"),
            "storageContainer": obj.get("storageContainer"),
            "storageContainerName": obj.get("storageContainerName"),
            "storageResourceGroup": obj.get("storageResourceGroup"),
            "storageResourceGroupName": obj.get("storageResourceGroupName")
        })
        return _obj


