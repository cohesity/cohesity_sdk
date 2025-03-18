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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.object_ms_team_param import ObjectMsTeamParam
from cohesity_sdk.helios.models.recovery_object_identifier import RecoveryObjectIdentifier
from cohesity_sdk.helios.models.target_ms_team_param import TargetMsTeamParam
from typing import Set
from typing_extensions import Self

class RecoverMsTeamParams(BaseModel):
    """
    Specifies the parameters to recover Microsoft 365 Teams.
    """ # noqa: E501
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue recovering other teams, if some of the teams fail to recover. Default value is false.", alias="continueOnError")
    create_new_team: Optional[StrictBool] = Field(default=None, description="Specifies to create new team in case the target team doesn't exists in case restoreToOriginal is false.", alias="createNewTeam")
    objects: Optional[List[ObjectMsTeamParam]] = Field(description="Specifies a list of Microsoft 365 Teams params associated with objects to recover.")
    restore_original_owners: Optional[StrictBool] = Field(default=None, description="Specifies if the original members/owners should be part of the newly created target team or not.", alias="restoreOriginalOwners")
    restore_to_original: Optional[StrictBool] = Field(default=None, description="Specifies whether or not all Microsoft 365 Teams are restored to original location.", alias="restoreToOriginal")
    target_ms_team: Optional[TargetMsTeamParam] = Field(default=None, description="This field is deprecated. Use targetTeamNickName and targetTeamFullName instead.", alias="targetMsTeam")
    target_ms_team_param: Optional[TargetMsTeamParam] = Field(default=None, description="Specifies the ms team target parameters in case of restoreToOriginal is false.", alias="targetMsTeamParam")
    target_team_full_name: Optional[StrictStr] = Field(default=None, description="This field is deprecated. Specifies target team name in case restoreToOriginal is false. This will be ignored if restoring to alternate existing team (i.e. to a team the nickname of which is same as the one supplied by the end user).", alias="targetTeamFullName")
    target_team_name: Optional[StrictStr] = Field(default=None, description="Specifies the target team name in case restoreToOriginal is false.", alias="targetTeamName")
    target_team_nick_name: Optional[StrictStr] = Field(default=None, description="This field is deprecated. Specifies target team nickname in case restoreToOriginal is false.", alias="targetTeamNickName")
    target_team_owner: Optional[RecoveryObjectIdentifier] = Field(default=None, description="Specifies the additional owner entity info for the selected target team.", alias="targetTeamOwner")
    __properties: ClassVar[List[str]] = ["continueOnError", "createNewTeam", "objects", "restoreOriginalOwners", "restoreToOriginal", "targetMsTeam", "targetMsTeamParam", "targetTeamFullName", "targetTeamName", "targetTeamNickName", "targetTeamOwner"]

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
        """Create an instance of RecoverMsTeamParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of target_ms_team
        if self.target_ms_team:
            _dict['targetMsTeam'] = self.target_ms_team.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_ms_team_param
        if self.target_ms_team_param:
            _dict['targetMsTeamParam'] = self.target_ms_team_param.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_team_owner
        if self.target_team_owner:
            _dict['targetTeamOwner'] = self.target_team_owner.to_dict()
        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if create_new_team (nullable) is None
        # and model_fields_set contains the field
        if self.create_new_team is None and "create_new_team" in self.model_fields_set:
            _dict['createNewTeam'] = None

        # set to None if objects (nullable) is None
        # and model_fields_set contains the field
        if self.objects is None and "objects" in self.model_fields_set:
            _dict['objects'] = None

        # set to None if restore_original_owners (nullable) is None
        # and model_fields_set contains the field
        if self.restore_original_owners is None and "restore_original_owners" in self.model_fields_set:
            _dict['restoreOriginalOwners'] = None

        # set to None if restore_to_original (nullable) is None
        # and model_fields_set contains the field
        if self.restore_to_original is None and "restore_to_original" in self.model_fields_set:
            _dict['restoreToOriginal'] = None

        # set to None if target_team_full_name (nullable) is None
        # and model_fields_set contains the field
        if self.target_team_full_name is None and "target_team_full_name" in self.model_fields_set:
            _dict['targetTeamFullName'] = None

        # set to None if target_team_name (nullable) is None
        # and model_fields_set contains the field
        if self.target_team_name is None and "target_team_name" in self.model_fields_set:
            _dict['targetTeamName'] = None

        # set to None if target_team_nick_name (nullable) is None
        # and model_fields_set contains the field
        if self.target_team_nick_name is None and "target_team_nick_name" in self.model_fields_set:
            _dict['targetTeamNickName'] = None

        # set to None if target_team_owner (nullable) is None
        # and model_fields_set contains the field
        if self.target_team_owner is None and "target_team_owner" in self.model_fields_set:
            _dict['targetTeamOwner'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverMsTeamParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "continueOnError": obj.get("continueOnError"),
            "createNewTeam": obj.get("createNewTeam"),
            "objects": [ObjectMsTeamParam.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "restoreOriginalOwners": obj.get("restoreOriginalOwners"),
            "restoreToOriginal": obj.get("restoreToOriginal"),
            "targetMsTeam": TargetMsTeamParam.from_dict(obj["targetMsTeam"]) if obj.get("targetMsTeam") is not None else None,
            "targetMsTeamParam": TargetMsTeamParam.from_dict(obj["targetMsTeamParam"]) if obj.get("targetMsTeamParam") is not None else None,
            "targetTeamFullName": obj.get("targetTeamFullName"),
            "targetTeamName": obj.get("targetTeamName"),
            "targetTeamNickName": obj.get("targetTeamNickName"),
            "targetTeamOwner": RecoveryObjectIdentifier.from_dict(obj["targetTeamOwner"]) if obj.get("targetTeamOwner") is not None else None
        })
        return _obj


