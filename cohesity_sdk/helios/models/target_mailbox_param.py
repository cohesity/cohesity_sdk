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

class TargetMailboxParam(BaseModel):
    """
    Specifies the target Mailbox to recover to.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the target mailbox. Atleast one of id or primarySMTPAddress need to be defined. In case both id and primarySMTPAddress are defined then id takes precedence.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the object.")
    parent_source_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the domain for alternate domain recovery.", alias="parentSourceId")
    primary_smtp_address: Optional[StrictStr] = Field(default=None, description="Specifies the primary SMTP address of the target mailbox. Atleast one of id or primarySMTPAddress needs to be defined. In case both id and primarySMTPAddress are defined then id takes precedence.", alias="primarySmtpAddress")
    target_folder_path: Optional[StrictStr] = Field(description="Specifies the path to the target folder.", alias="targetFolderPath")
    __properties: ClassVar[List[str]] = ["id", "name", "parentSourceId", "primarySmtpAddress", "targetFolderPath"]

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
        """Create an instance of TargetMailboxParam from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if parent_source_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_source_id is None and "parent_source_id" in self.model_fields_set:
            _dict['parentSourceId'] = None

        # set to None if primary_smtp_address (nullable) is None
        # and model_fields_set contains the field
        if self.primary_smtp_address is None and "primary_smtp_address" in self.model_fields_set:
            _dict['primarySmtpAddress'] = None

        # set to None if target_folder_path (nullable) is None
        # and model_fields_set contains the field
        if self.target_folder_path is None and "target_folder_path" in self.model_fields_set:
            _dict['targetFolderPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TargetMailboxParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "parentSourceId": obj.get("parentSourceId"),
            "primarySmtpAddress": obj.get("primarySmtpAddress"),
            "targetFolderPath": obj.get("targetFolderPath")
        })
        return _obj


