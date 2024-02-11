from typing import Dict, Type
from folder_solvers.base_solver import BaseSolver
from folder_solvers.constant import ConstantSolver
from folder_solvers.linear import LinearSolver
from folder_solvers.quadratic import QuadraticSolver


solver_name_to_SolverClass : Dict[str, Type[BaseSolver]] = {
    "constant" : ConstantSolver,
    "linear" : LinearSolver,
    "quadratic" : QuadraticSolver,
}