from typing import Any, Union
import inspect

from facefusion.typing import State, StateSet, StateContext, StateKey
from facefusion.processors.frame.typing import FrameProcessorState, FrameProcessorStateKey

STATES : Union[StateSet, FrameProcessorState] =\
{
	'core': {}, #type:ignore[typeddict-item]
	'uis': {} #type:ignore[typeddict-item]
}


def get_state() -> Union[State, FrameProcessorState]:
	state_context = detect_state_context()
	return STATES.get(state_context) #type:ignore


def init_item(key : Union[StateKey, FrameProcessorStateKey], value : Any) -> None:
	STATES['core'][key] = value #type:ignore
	STATES['uis'][key] = value #type:ignore


def get_item(key : Union[StateKey, FrameProcessorStateKey]) -> Any:
	return get_state().get(key) #type:ignore


def set_item(key : Union[StateKey, FrameProcessorStateKey], value : Any) -> None:
	state_context = detect_state_context()
	STATES[state_context][key] = value #type:ignore


def clear_item(key : Union[StateKey, FrameProcessorStateKey]) -> None:
	set_item(key, None)


def detect_state_context() -> StateContext:
	for stack in inspect.stack():
		if 'facefusion/uis' in stack.filename:
			return 'uis'
	return 'core'
