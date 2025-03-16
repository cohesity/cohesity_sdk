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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.nas_qos_policy import NasQosPolicy
from cohesity_sdk.cluster.models.recovery_vlan_config import RecoveryVlanConfig
from typing import Optional, Set
from typing_extensions import Self

class RecoverNasVolumeToViewParams(BaseModel):
    """
    Specifies the recovery target configuration if NAS volumes are being recovered as a Cohesity view.
    """ # noqa: E501
    qos_policy: Optional[NasQosPolicy] = Field(default=None, alias="qosPolicy")
    view_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the view.", alias="viewName")
    vlan_config: Optional[RecoveryVlanConfig] = Field(default=None, alias="vlanConfig")
    __properties: ClassVar[List[str]] = ["qosPolicy", "viewName", "vlanConfig"]

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
        """Create an instance of RecoverNasVolumeToViewParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of qos_policy
        if self.qos_policy:
            _dict['qosPolicy'] = self.qos_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vlan_config
        if self.vlan_config:
            _dict['vlanConfig'] = self.vlan_config.to_dict()
        # set to None if view_name (nullable) is None
        # and model_fields_set contains the field
        if self.view_name is None and "view_name" in self.model_fields_set:
            _dict['viewName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverNasVolumeToViewParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "qosPolicy": NasQosPolicy.from_dict(obj["qosPolicy"]) if obj.get("qosPolicy") is not None else None,
            "viewName": obj.get("viewName"),
            "vlanConfig": RecoveryVlanConfig.from_dict(obj["vlanConfig"]) if obj.get("vlanConfig") is not None else None
        })
        return _obj


