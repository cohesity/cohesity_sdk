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
from cohesity_sdk.cluster.models.object_mailbox_param import ObjectMailboxParam
from cohesity_sdk.cluster.models.pst_param import PstParam
from cohesity_sdk.cluster.models.target_mailbox_param import TargetMailboxParam
from typing import Set
from typing_extensions import Self

class RecoverMailboxParams(BaseModel):
    """
    Specifies the parameters to recover an Office 365 Mailbox.
    """ # noqa: E501
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue recovering other Mailboxes if one of Mailbox failed to recover. Default value is false.", alias="continueOnError")
    objects: Optional[List[ObjectMailboxParam]] = Field(description="Specifies a list of Mailbox params associated with the objects to recover.")
    pst_params: Optional[PstParam] = Field(default=None, alias="pstParams")
    skip_recover_archive_mailbox: Optional[StrictBool] = Field(default=None, description="Specifies whether to skip the recovery of the archive mailbox and/or items present in the archive mailbox. Default value is true", alias="skipRecoverArchiveMailbox")
    skip_recover_archive_recoverable_items: Optional[StrictBool] = Field(default=None, description="Specifies whether to skip the recovery of the Archive Recoverable Items present in the selected snapshot. Default value is true", alias="skipRecoverArchiveRecoverableItems")
    skip_recover_recoverable_items: Optional[StrictBool] = Field(default=None, description="Specifies whether to skip the recovery of the Recoverable Items present in the selected snapshot. Default value is true", alias="skipRecoverRecoverableItems")
    target_mailbox: Optional[TargetMailboxParam] = Field(default=None, alias="targetMailbox")
    __properties: ClassVar[List[str]] = ["continueOnError", "objects", "pstParams", "skipRecoverArchiveMailbox", "skipRecoverArchiveRecoverableItems", "skipRecoverRecoverableItems", "targetMailbox"]

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
        """Create an instance of RecoverMailboxParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pst_params
        if self.pst_params:
            _dict['pstParams'] = self.pst_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_mailbox
        if self.target_mailbox:
            _dict['targetMailbox'] = self.target_mailbox.to_dict()
        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if objects (nullable) is None
        # and model_fields_set contains the field
        if self.objects is None and "objects" in self.model_fields_set:
            _dict['objects'] = None

        # set to None if skip_recover_archive_mailbox (nullable) is None
        # and model_fields_set contains the field
        if self.skip_recover_archive_mailbox is None and "skip_recover_archive_mailbox" in self.model_fields_set:
            _dict['skipRecoverArchiveMailbox'] = None

        # set to None if skip_recover_archive_recoverable_items (nullable) is None
        # and model_fields_set contains the field
        if self.skip_recover_archive_recoverable_items is None and "skip_recover_archive_recoverable_items" in self.model_fields_set:
            _dict['skipRecoverArchiveRecoverableItems'] = None

        # set to None if skip_recover_recoverable_items (nullable) is None
        # and model_fields_set contains the field
        if self.skip_recover_recoverable_items is None and "skip_recover_recoverable_items" in self.model_fields_set:
            _dict['skipRecoverRecoverableItems'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverMailboxParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "continueOnError": obj.get("continueOnError"),
            "objects": [ObjectMailboxParam.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "pstParams": PstParam.from_dict(obj["pstParams"]) if obj.get("pstParams") is not None else None,
            "skipRecoverArchiveMailbox": obj.get("skipRecoverArchiveMailbox"),
            "skipRecoverArchiveRecoverableItems": obj.get("skipRecoverArchiveRecoverableItems"),
            "skipRecoverRecoverableItems": obj.get("skipRecoverRecoverableItems"),
            "targetMailbox": TargetMailboxParam.from_dict(obj["targetMailbox"]) if obj.get("targetMailbox") is not None else None
        })
        return _obj


