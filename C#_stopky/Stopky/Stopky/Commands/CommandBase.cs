using System;
using System.Windows.Input;

namespace Stopky.Commands;

public abstract class CommandBase: ICommand{
    public virtual bool CanExecute(object? parameter){
        return true;
    }

    public abstract void Execute(object? parameter);

    protected void OnCanExecutedChanged(){
        CanExecuteChanged?.Invoke(this, new EventArgs());
    }

    public event EventHandler? CanExecuteChanged;
}