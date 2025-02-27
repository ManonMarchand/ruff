use crate::prelude::*;
use ruff_python_ast::{Constant, PatternMatchSingleton};

use crate::{FormatNodeRule, PyFormatter};

#[derive(Default)]
pub struct FormatPatternMatchSingleton;

impl FormatNodeRule<PatternMatchSingleton> for FormatPatternMatchSingleton {
    fn fmt_fields(&self, item: &PatternMatchSingleton, f: &mut PyFormatter) -> FormatResult<()> {
        match item.value {
            Constant::None => text("None").fmt(f),
            Constant::Bool(true) => text("True").fmt(f),
            Constant::Bool(false) => text("False").fmt(f),
            _ => unreachable!(),
        }
    }
}
