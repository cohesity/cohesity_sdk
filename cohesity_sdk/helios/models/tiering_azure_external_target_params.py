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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.azure_hot_blob_params import AzureHotBlobParams
from typing import Optional, Set
from typing_extensions import Self

class TieringAzureExternalTargetParams(BaseModel):
    """
    Specifies the common parameters which are specific to Azure related External Targets.
    """ # noqa: E501
    client_id: Optional[StrictStr] = Field(default=None, description="Specifies the client id of the managed identity assigned to the cluster This is used only for clusters running as Azure VMs where authentication is done using AD.", alias="clientId")
    container_name: Optional[StrictStr] = Field(description="Specifies the container name of the external target.", alias="containerName")
    region: Optional[StrictStr] = Field(default=None, description="Specifies region of the External Target. This is only populated for FortKnox vaults.")
    storage_access_key: Optional[StrictStr] = Field(default=None, description="Specifies the storage access key of the external target.", alias="storageAccessKey")
    storage_account_name: Optional[StrictStr] = Field(description="Specifies the storage account name of the external target.", alias="storageAccountName")
    storage_class: Optional[StrictStr] = Field(description="Specifies the Azure External Target class.", alias="storageClass")
    hot_blob_params: Optional[AzureHotBlobParams] = Field(default=None, alias="hotBlobParams")
    __properties: ClassVar[List[str]] = ["clientId", "containerName", "region", "storageAccessKey", "storageAccountName", "storageClass", "hotBlobParams"]

    @field_validator('storage_class')
    def storage_class_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AzureHotBlob']):
            raise ValueError("must be one of enum values ('AzureHotBlob')")
        return value

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
        """Create an instance of TieringAzureExternalTargetParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of hot_blob_params
        if self.hot_blob_params:
            _dict['hotBlobParams'] = self.hot_blob_params.to_dict()
        # set to None if client_id (nullable) is None
        # and model_fields_set contains the field
        if self.client_id is None and "client_id" in self.model_fields_set:
            _dict['clientId'] = None

        # set to None if container_name (nullable) is None
        # and model_fields_set contains the field
        if self.container_name is None and "container_name" in self.model_fields_set:
            _dict['containerName'] = None

        # set to None if region (nullable) is None
        # and model_fields_set contains the field
        if self.region is None and "region" in self.model_fields_set:
            _dict['region'] = None

        # set to None if storage_access_key (nullable) is None
        # and model_fields_set contains the field
        if self.storage_access_key is None and "storage_access_key" in self.model_fields_set:
            _dict['storageAccessKey'] = None

        # set to None if storage_account_name (nullable) is None
        # and model_fields_set contains the field
        if self.storage_account_name is None and "storage_account_name" in self.model_fields_set:
            _dict['storageAccountName'] = None

        # set to None if storage_class (nullable) is None
        # and model_fields_set contains the field
        if self.storage_class is None and "storage_class" in self.model_fields_set:
            _dict['storageClass'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TieringAzureExternalTargetParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clientId": obj.get("clientId"),
            "containerName": obj.get("containerName"),
            "region": obj.get("region"),
            "storageAccessKey": obj.get("storageAccessKey"),
            "storageAccountName": obj.get("storageAccountName"),
            "storageClass": obj.get("storageClass"),
            "hotBlobParams": AzureHotBlobParams.from_dict(obj["hotBlobParams"]) if obj.get("hotBlobParams") is not None else None
        })
        return _obj


