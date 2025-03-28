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
from cohesity_sdk.cluster.models.common_recover_oracle_app_target_params import CommonRecoverOracleAppTargetParams
from cohesity_sdk.cluster.models.recovery_vlan_config import RecoveryVlanConfig
from typing import Set
from typing_extensions import Self

class RecoverOracleAppParams(BaseModel):
    """
    Specifies the parameters to recover Oracle databases.
    """ # noqa: E501
    oracle_target_params: Optional[CommonRecoverOracleAppTargetParams] = Field(default=None, alias="oracleTargetParams")
    target_environment: StrictStr = Field(description="Specifies the environment of the recovery target. The corresponding params below must be filled out.", alias="targetEnvironment")
    vlan_config: Optional[RecoveryVlanConfig] = Field(default=None, alias="vlanConfig")
    __properties: ClassVar[List[str]] = ["oracleTargetParams", "targetEnvironment", "vlanConfig"]

    @field_validator('target_environment')
    def target_environment_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['kOracle']):
            raise ValueError("must be one of enum values ('kOracle')")
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
        """Create an instance of RecoverOracleAppParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of oracle_target_params
        if self.oracle_target_params:
            _dict['oracleTargetParams'] = self.oracle_target_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vlan_config
        if self.vlan_config:
            _dict['vlanConfig'] = self.vlan_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverOracleAppParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "oracleTargetParams": CommonRecoverOracleAppTargetParams.from_dict(obj["oracleTargetParams"]) if obj.get("oracleTargetParams") is not None else None,
            "targetEnvironment": obj.get("targetEnvironment"),
            "vlanConfig": RecoveryVlanConfig.from_dict(obj["vlanConfig"]) if obj.get("vlanConfig") is not None else None
        })
        return _obj


