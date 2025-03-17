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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.recover_vmware_vm_new_source_network_config import RecoverVmwareVmNewSourceNetworkConfig
from cohesity_sdk.cluster.models.recovery_object_identifier import RecoveryObjectIdentifier
from typing import Set
from typing_extensions import Self

class RecoverVmwareVmVCenterSourceConfig(BaseModel):
    """
    Specifies the new destination Source configuration where the VMs will be recovered for vCenter sources.
    """ # noqa: E501
    datastores: Optional[List[RecoveryObjectIdentifier]] = Field(description="Specifies the datastore objects where the object's files should be recovered to.")
    network_config: Optional[RecoverVmwareVmNewSourceNetworkConfig] = Field(default=None, alias="networkConfig")
    resource_pool: RecoveryObjectIdentifier = Field(alias="resourcePool")
    source: RecoveryObjectIdentifier
    vm_folder: Optional[RecoveryObjectIdentifier] = Field(default=None, alias="vmFolder")
    __properties: ClassVar[List[str]] = ["datastores", "networkConfig", "resourcePool", "source", "vmFolder"]

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
        """Create an instance of RecoverVmwareVmVCenterSourceConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in datastores (list)
        _items = []
        if self.datastores:
            for _item_datastores in self.datastores:
                if _item_datastores:
                    _items.append(_item_datastores.to_dict())
            _dict['datastores'] = _items
        # override the default output from pydantic by calling `to_dict()` of network_config
        if self.network_config:
            _dict['networkConfig'] = self.network_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_pool
        if self.resource_pool:
            _dict['resourcePool'] = self.resource_pool.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vm_folder
        if self.vm_folder:
            _dict['vmFolder'] = self.vm_folder.to_dict()
        # set to None if datastores (nullable) is None
        # and model_fields_set contains the field
        if self.datastores is None and "datastores" in self.model_fields_set:
            _dict['datastores'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverVmwareVmVCenterSourceConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "datastores": [RecoveryObjectIdentifier.from_dict(_item) for _item in obj["datastores"]] if obj.get("datastores") is not None else None,
            "networkConfig": RecoverVmwareVmNewSourceNetworkConfig.from_dict(obj["networkConfig"]) if obj.get("networkConfig") is not None else None,
            "resourcePool": RecoveryObjectIdentifier.from_dict(obj["resourcePool"]) if obj.get("resourcePool") is not None else None,
            "source": RecoveryObjectIdentifier.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "vmFolder": RecoveryObjectIdentifier.from_dict(obj["vmFolder"]) if obj.get("vmFolder") is not None else None
        })
        return _obj


