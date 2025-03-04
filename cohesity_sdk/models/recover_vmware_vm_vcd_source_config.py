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
from cohesity_sdk.models.org_vdc_network import OrgVDCNetwork
from cohesity_sdk.models.recover_vmware_vm_new_source_network_config import RecoverVmwareVmNewSourceNetworkConfig
from cohesity_sdk.models.recovery_object_identifier import RecoveryObjectIdentifier
from cohesity_sdk.models.vcd_storage_profile_params import VcdStorageProfileParams
from typing import Optional, Set
from typing_extensions import Self

class RecoverVmwareVmVCDSourceConfig(BaseModel):
    """
    Specifies the new destination Source configuration where the VMs will be recovered for vCloudDirector sources.
    """ # noqa: E501
    datastores: Optional[List[RecoveryObjectIdentifier]] = Field(default=None, description="Specifies the datastore objects where the object's files should be recovered to. This should only be specified if storageProfile is not specified.")
    network_config: Optional[RecoverVmwareVmNewSourceNetworkConfig] = Field(default=None, alias="networkConfig")
    org_vdc_network: Optional[OrgVDCNetwork] = Field(default=None, alias="orgVdcNetwork")
    source: RecoveryObjectIdentifier
    storage_profile: Optional[VcdStorageProfileParams] = Field(default=None, alias="storageProfile")
    v_app: Optional[RecoveryObjectIdentifier] = Field(default=None, alias="vApp")
    vdc: RecoveryObjectIdentifier
    __properties: ClassVar[List[str]] = ["datastores", "networkConfig", "orgVdcNetwork", "source", "storageProfile", "vApp", "vdc"]

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
        """Create an instance of RecoverVmwareVmVCDSourceConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of org_vdc_network
        if self.org_vdc_network:
            _dict['orgVdcNetwork'] = self.org_vdc_network.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage_profile
        if self.storage_profile:
            _dict['storageProfile'] = self.storage_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of v_app
        if self.v_app:
            _dict['vApp'] = self.v_app.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vdc
        if self.vdc:
            _dict['vdc'] = self.vdc.to_dict()
        # set to None if datastores (nullable) is None
        # and model_fields_set contains the field
        if self.datastores is None and "datastores" in self.model_fields_set:
            _dict['datastores'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverVmwareVmVCDSourceConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "datastores": [RecoveryObjectIdentifier.from_dict(_item) for _item in obj["datastores"]] if obj.get("datastores") is not None else None,
            "networkConfig": RecoverVmwareVmNewSourceNetworkConfig.from_dict(obj["networkConfig"]) if obj.get("networkConfig") is not None else None,
            "orgVdcNetwork": OrgVDCNetwork.from_dict(obj["orgVdcNetwork"]) if obj.get("orgVdcNetwork") is not None else None,
            "source": RecoveryObjectIdentifier.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "storageProfile": VcdStorageProfileParams.from_dict(obj["storageProfile"]) if obj.get("storageProfile") is not None else None,
            "vApp": RecoveryObjectIdentifier.from_dict(obj["vApp"]) if obj.get("vApp") is not None else None,
            "vdc": RecoveryObjectIdentifier.from_dict(obj["vdc"]) if obj.get("vdc") is not None else None
        })
        return _obj


