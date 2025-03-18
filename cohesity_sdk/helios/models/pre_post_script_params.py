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
from cohesity_sdk.helios.models.common_post_backup_script_params import CommonPostBackupScriptParams
from cohesity_sdk.helios.models.common_pre_backup_script_params import CommonPreBackupScriptParams
from typing import Set
from typing_extensions import Self

class PrePostScriptParams(BaseModel):
    """
    Specifies the params for pre and post scripts.
    """ # noqa: E501
    post_script: Optional[CommonPostBackupScriptParams] = Field(default=None, alias="postScript")
    pre_script: Optional[CommonPreBackupScriptParams] = Field(default=None, alias="preScript")
    __properties: ClassVar[List[str]] = ["postScript", "preScript"]

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
        """Create an instance of PrePostScriptParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of post_script
        if self.post_script:
            _dict['postScript'] = self.post_script.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pre_script
        if self.pre_script:
            _dict['preScript'] = self.pre_script.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrePostScriptParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "postScript": CommonPostBackupScriptParams.from_dict(obj["postScript"]) if obj.get("postScript") is not None else None,
            "preScript": CommonPreBackupScriptParams.from_dict(obj["preScript"]) if obj.get("preScript") is not None else None
        })
        return _obj


