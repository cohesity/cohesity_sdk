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
from cohesity_sdk.helios.models.cluster_identifier import ClusterIdentifier
from typing import Optional, Set
from typing_extensions import Self

class CancelObjectRunParams(BaseModel):
    """
    One object run to cancel.
    """ # noqa: E501
    archival_target_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the archival target ids where the tasks run. If specified, the archival target ids must be present within the run specified by the runId above.", alias="archivalTargetIds")
    cancel_local_run: Optional[StrictBool] = Field(default=None, description="Specifies whether to cancel the local backup run. Default is false.", alias="cancelLocalRun")
    cloud_spin_target_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the cloud spin target ids where the tasks run. If specified, the archival target ids must be present within the run specified by the runId above.", alias="cloudSpinTargetIds")
    replication_targets: Optional[List[ClusterIdentifier]] = Field(default=None, description="Specifies the cluster identifiers where the tasks run. If specified, the archival target ids must be present within the run specified by the runId above.", alias="replicationTargets")
    run_id: Optional[StrictStr] = Field(description="Specifies the id of the run to cancel.", alias="runId")
    __properties: ClassVar[List[str]] = ["archivalTargetIds", "cancelLocalRun", "cloudSpinTargetIds", "replicationTargets", "runId"]

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
        """Create an instance of CancelObjectRunParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in replication_targets (list)
        _items = []
        if self.replication_targets:
            for _item_replication_targets in self.replication_targets:
                if _item_replication_targets:
                    _items.append(_item_replication_targets.to_dict())
            _dict['replicationTargets'] = _items
        # set to None if archival_target_ids (nullable) is None
        # and model_fields_set contains the field
        if self.archival_target_ids is None and "archival_target_ids" in self.model_fields_set:
            _dict['archivalTargetIds'] = None

        # set to None if cancel_local_run (nullable) is None
        # and model_fields_set contains the field
        if self.cancel_local_run is None and "cancel_local_run" in self.model_fields_set:
            _dict['cancelLocalRun'] = None

        # set to None if cloud_spin_target_ids (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_spin_target_ids is None and "cloud_spin_target_ids" in self.model_fields_set:
            _dict['cloudSpinTargetIds'] = None

        # set to None if replication_targets (nullable) is None
        # and model_fields_set contains the field
        if self.replication_targets is None and "replication_targets" in self.model_fields_set:
            _dict['replicationTargets'] = None

        # set to None if run_id (nullable) is None
        # and model_fields_set contains the field
        if self.run_id is None and "run_id" in self.model_fields_set:
            _dict['runId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CancelObjectRunParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archivalTargetIds": obj.get("archivalTargetIds"),
            "cancelLocalRun": obj.get("cancelLocalRun"),
            "cloudSpinTargetIds": obj.get("cloudSpinTargetIds"),
            "replicationTargets": [ClusterIdentifier.from_dict(_item) for _item in obj["replicationTargets"]] if obj.get("replicationTargets") is not None else None,
            "runId": obj.get("runId")
        })
        return _obj


