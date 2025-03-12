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
from typing import Any, ClassVar, Dict, List
from cohesity_sdk.helios.models.common_recover_object_snapshot_params import CommonRecoverObjectSnapshotParams
from cohesity_sdk.helios.models.ms_team_param import MsTeamParam
from typing import Optional, Set
from typing_extensions import Self

class ObjectMsTeamParam(BaseModel):
    """
    Specifies recovery parameters associated with a Microsoft 365 Team.
    """ # noqa: E501
    ms_team_param: MsTeamParam = Field(alias="msTeamParam")
    recover_object: CommonRecoverObjectSnapshotParams = Field(alias="recoverObject")
    __properties: ClassVar[List[str]] = ["msTeamParam", "recoverObject"]

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
        """Create an instance of ObjectMsTeamParam from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ms_team_param
        if self.ms_team_param:
            _dict['msTeamParam'] = self.ms_team_param.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recover_object
        if self.recover_object:
            _dict['recoverObject'] = self.recover_object.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectMsTeamParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "msTeamParam": MsTeamParam.from_dict(obj["msTeamParam"]) if obj.get("msTeamParam") is not None else None,
            "recoverObject": CommonRecoverObjectSnapshotParams.from_dict(obj["recoverObject"]) if obj.get("recoverObject") is not None else None
        })
        return _obj


