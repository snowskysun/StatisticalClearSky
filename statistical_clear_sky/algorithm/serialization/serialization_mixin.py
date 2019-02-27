"""
This module defines Mixin for serialization.
"""
import json
import numpy as np
from statistical_clear_sky.algorithm.serialization.state_data import StateData

class SerializationMixin(object):

    def save_instance(self, filepath):
        save_dict = dict(
            power_signals_d = self._state_data.power_signals_d.tolist(),
            rank_k = self._state_data.rank_k,
            matrix_l0 = self._state_data.matrix_l0.tolist(),
            matrix_r0 = self._state_data.matrix_r0.tolist(),
            l_value = self._state_data.l_value.tolist(),
            r_value = self._state_data.r_value.tolist(),
            beta_value = float(self._state_data.beta_value),
            component_r0 = self._state_data.component_r0.tolist(),
            mu_l = self._state_data.mu_l,
            mu_r = self._state_data.mu_r,
            tau = self._state_data._tau,
            is_solver_error = self._state_data.is_solver_error,
            is_problem_status_error = self._state_data.is_problem_status_error,
            f1_increase = self._state_data.f1_increase,
            obj_increase = self._state_data.obj_increase,
            residuals_median = self._state_data.residuals_median,
            residuals_variance = self._state_data.residuals_variance,
            residual_l0_norm = self._state_data.residual_l0_norm,
            weights = self._state_data.weights.tolist()
        )
        with open(filepath, 'w') as file:
            json.dump(save_dict, file)

    @classmethod
    def load_instance(cls, filepath):
        with open(filepath, 'r') as file:
            load_dict = json.load(file)

        instance = cls(np.array(load_dict['power_signals_d']),
                       rank_k=load_dict['rank_k'])

        instance._matrix_l0 = np.array(load_dict['matrix_l0'])
        instance._matrix_r0 = np.array(load_dict['matrix_r0'])

        instance._l_cs.value = np.array(load_dict['l_value'])
        instance._r_cs.value = np.array(load_dict['r_value'])
        instance._beta.value = load_dict['beta_value']

        instance._component_r0 = np.array(load_dict['component_r0'])

        instance._mu_l = load_dict['mu_l']
        instance._mu_r = load_dict['mu_r']
        instance._tau = load_dict['tau']
        instance._state_data.is_solver_error = load_dict['is_solver_error']
        instance._state_data.is_problem_status_error = load_dict[
                                                'is_problem_status_error']
        instance._state_data.f1_increase = load_dict['f1_increase']
        instance._state_data.obj_increase = load_dict['obj_increase']
        instance._residuals_median = load_dict['residuals_median']
        instance._residuals_variance = load_dict['residuals_variance']
        instance._residual_l0_norm = load_dict['residual_l0_norm']

        instance._weights = np.array(load_dict['weights'])

        return instance
