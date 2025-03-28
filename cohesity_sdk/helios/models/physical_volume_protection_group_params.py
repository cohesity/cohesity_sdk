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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.helios.models.indexing_policy import IndexingPolicy
from cohesity_sdk.helios.models.physical_volume_protection_group_object_params import PhysicalVolumeProtectionGroupObjectParams
from cohesity_sdk.helios.models.pre_post_script_params import PrePostScriptParams
from typing import Set
from typing_extensions import Self

class PhysicalVolumeProtectionGroupParams(BaseModel):
    """
    Specifies the parameters which are specific to Volume based physical Protection Groups.
    """ # noqa: E501
    cobmr_backup: Optional[StrictBool] = Field(default=None, description="Specifies whether to take a CoBMR backup.", alias="cobmrBackup")
    continue_on_quiesce_failure: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue backing up on quiesce failure", alias="continueOnQuiesceFailure")
    dedup_exclusion_source_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies ids of sources for which deduplication has to be disabled.", alias="dedupExclusionSourceIds")
    excluded_vss_writers: Optional[List[StrictStr]] = Field(default=None, description="Specifies writer names which should be excluded from physical volume based backups.", alias="excludedVssWriters")
    incremental_backup_after_restart: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to perform an incremental backup after the server restarts. This is applicable to windows environments.", alias="incrementalBackupAfterRestart")
    indexing_policy: Optional[IndexingPolicy] = Field(default=None, alias="indexingPolicy")
    objects: Annotated[List[PhysicalVolumeProtectionGroupObjectParams], Field(min_length=1)]
    perform_source_side_deduplication: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to perform source side deduplication on this Protection Group.", alias="performSourceSideDeduplication")
    pre_post_script: Optional[PrePostScriptParams] = Field(default=None, alias="prePostScript")
    quiesce: Optional[StrictBool] = Field(default=None, description="Specifies Whether to take app-consistent snapshots by quiescing apps and the filesystem before taking a backup")
    __properties: ClassVar[List[str]] = ["cobmrBackup", "continueOnQuiesceFailure", "dedupExclusionSourceIds", "excludedVssWriters", "incrementalBackupAfterRestart", "indexingPolicy", "objects", "performSourceSideDeduplication", "prePostScript", "quiesce"]

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
        """Create an instance of PhysicalVolumeProtectionGroupParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of indexing_policy
        if self.indexing_policy:
            _dict['indexingPolicy'] = self.indexing_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of pre_post_script
        if self.pre_post_script:
            _dict['prePostScript'] = self.pre_post_script.to_dict()
        # set to None if cobmr_backup (nullable) is None
        # and model_fields_set contains the field
        if self.cobmr_backup is None and "cobmr_backup" in self.model_fields_set:
            _dict['cobmrBackup'] = None

        # set to None if continue_on_quiesce_failure (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_quiesce_failure is None and "continue_on_quiesce_failure" in self.model_fields_set:
            _dict['continueOnQuiesceFailure'] = None

        # set to None if excluded_vss_writers (nullable) is None
        # and model_fields_set contains the field
        if self.excluded_vss_writers is None and "excluded_vss_writers" in self.model_fields_set:
            _dict['excludedVssWriters'] = None

        # set to None if incremental_backup_after_restart (nullable) is None
        # and model_fields_set contains the field
        if self.incremental_backup_after_restart is None and "incremental_backup_after_restart" in self.model_fields_set:
            _dict['incrementalBackupAfterRestart'] = None

        # set to None if perform_source_side_deduplication (nullable) is None
        # and model_fields_set contains the field
        if self.perform_source_side_deduplication is None and "perform_source_side_deduplication" in self.model_fields_set:
            _dict['performSourceSideDeduplication'] = None

        # set to None if quiesce (nullable) is None
        # and model_fields_set contains the field
        if self.quiesce is None and "quiesce" in self.model_fields_set:
            _dict['quiesce'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PhysicalVolumeProtectionGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cobmrBackup": obj.get("cobmrBackup"),
            "continueOnQuiesceFailure": obj.get("continueOnQuiesceFailure"),
            "dedupExclusionSourceIds": obj.get("dedupExclusionSourceIds"),
            "excludedVssWriters": obj.get("excludedVssWriters"),
            "incrementalBackupAfterRestart": obj.get("incrementalBackupAfterRestart"),
            "indexingPolicy": IndexingPolicy.from_dict(obj["indexingPolicy"]) if obj.get("indexingPolicy") is not None else None,
            "objects": [PhysicalVolumeProtectionGroupObjectParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "performSourceSideDeduplication": obj.get("performSourceSideDeduplication"),
            "prePostScript": PrePostScriptParams.from_dict(obj["prePostScript"]) if obj.get("prePostScript") is not None else None,
            "quiesce": obj.get("quiesce")
        })
        return _obj


