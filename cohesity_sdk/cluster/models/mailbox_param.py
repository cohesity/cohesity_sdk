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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.folder_item import FolderItem
from typing import Set
from typing_extensions import Self

class MailboxParam(BaseModel):
    """
    Specifies parameters to recover a Mailbox.
    """ # noqa: E501
    recover_entire_mailbox: Optional[StrictBool] = Field(default=None, description="Specifies whether to recover the whole Mailbox.", alias="recoverEntireMailbox")
    recover_folders: Optional[List[FolderItem]] = Field(default=None, description="Specifies a list of email folders to recover.", alias="recoverFolders")
    __properties: ClassVar[List[str]] = ["recoverEntireMailbox", "recoverFolders"]

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
        """Create an instance of MailboxParam from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in recover_folders (list)
        _items = []
        if self.recover_folders:
            for _item_recover_folders in self.recover_folders:
                if _item_recover_folders:
                    _items.append(_item_recover_folders.to_dict())
            _dict['recoverFolders'] = _items
        # set to None if recover_entire_mailbox (nullable) is None
        # and model_fields_set contains the field
        if self.recover_entire_mailbox is None and "recover_entire_mailbox" in self.model_fields_set:
            _dict['recoverEntireMailbox'] = None

        # set to None if recover_folders (nullable) is None
        # and model_fields_set contains the field
        if self.recover_folders is None and "recover_folders" in self.model_fields_set:
            _dict['recoverFolders'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MailboxParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "recoverEntireMailbox": obj.get("recoverEntireMailbox"),
            "recoverFolders": [FolderItem.from_dict(_item) for _item in obj["recoverFolders"]] if obj.get("recoverFolders") is not None else None
        })
        return _obj


