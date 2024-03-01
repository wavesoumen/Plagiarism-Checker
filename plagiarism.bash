deactivate () {

#reset old environment variables

if [ "$ OLD_VIRTUAL_PATH:-}" ]; then PATH="${_OLD_VIRTUAL_PATH:-)" export PATH unset_OLD_VIRTUAL_PATH fl

if [ -n "$_OLD_VIRTUAL_PYTHONHOME:-)" ]; then PYTHONHOME="$(_OLD_VIRTUAL_PYTHONHOME:-}" export PYTHONHOME unset_OLD_VIRTUAL_PYTHONHOME

fl

I

# This should detect bash and zsh, which have a hash command that must # be called to get it to forget past commands. Without forgetting #past commands the $PATH changes we made may not be respected if [ -n "$(BASH:-)" -o-n "$(ZSH_VERSION:-}" ]; then hashr 2> /dev/null

fl

if [ -n "${OLD_VIRTUAL_PS1:-}" ]; then PS1="${_OLD_VIRTUAL_PS1:-}" export PS1 unset_OLD_VIRTUAL_PS1 fl

unset VIRTUAL_ENV unset VIRTUAL ENV PROMPT

if [ "$(1:-)" = "nondestructive" ]; then #Self destruct!
unset -f deactivate

fl

}

#unset irrelevant variables

deactivate nondestructive

VIRTUAL_ENV="/home/wave444/Desktop/plagiarism-checker-flask/venv"

export VIRTUAL_ENV

_OLD_VIRTUAL_PATH="$PATH"

PATH="$VIRTUAL_ENV/bin:$PATH" export PATH

#unset PYTHONHOME if set

# this will fall if PYTHONHOME is set to the empty string (which is b # could use if (set-u; : $PYTHONHOME); in bash

if [ -n "${PYTHONHOME:-}" ]; then _OLD_VIRTUAL_PYTHONHOME="${PYTHONHOME:-}"

unset PYTHONHOME

fi

if [ -z "${VIRTUAL_ENV_DISABLE_PROMPT:-}" ]; then _OLD_VIRTUAL_PS1="${PS1:-)"

PS1="(venv) ${PS1:-}" export PS1 VIRTUAL_ENV_PROMPT="(venv)

export VIRTUAL_ENV_PROMPT

fi
if [ -n "${BASH:-}" -o -n "${ZSH_VERSION:-}" ]; then hash -r 2> /dev/null

fi