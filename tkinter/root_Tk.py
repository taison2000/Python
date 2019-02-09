import tkinter

## ----------------------------------------------------------------------------
# >>> import tkinter
# >>> help(tkinter.Tk)
#

root = tkinter.Tk()

## ----------------------------------------------------------------------------
"""
# Methods : root.MethodName()
#   - __getattr__(self, attr)
#   - __init__(self, screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None)
#   - destroy(self)
#   - loadtk(self)
#   - readprofile(self, baseName, className)
#   - report_callback_exception(self, exc, val, tb)
#   - __getitem__ = cget(self, key)
#   - __setitem__(self, key, value)
#   - __str__(self)
#   - after(self, ms, func=None, *args)
#   - after_cancel(self, id)
#   - after_idle(self, func, *args)
#   - anchor = grid_anchor(self, anchor=None)
#   - bbox = grid_bbox(self, column=None, row=None, col2=None, row2=None)
#   - bell(self, displayof=0)
#   - bind(self, sequence=None, func=None, add=None)
#   - bind_all(self, sequence=None, func=None, add=None)
#   - bind_class(self, className, sequence=None, func=None, add=None)
#   - bindtags(self, tagList=None)
#   - cget(self, key)
#   - clipboard_append(self, string, **kw)
#   - clipboard_clear(self, **kw)
#   - clipboard_get(self, **kw)
#   - colormodel(self, value=None)
#   - columnconfigure = grid_columnconfigure(self, index, cnf={}, **kw)
#   - config = configure(self, cnf=None, **kw)
#   - configure(self, cnf=None, **kw)
#   - deletecommand(self, name)
#   - event_add(self, virtual, *sequences)
#   - event_delete(self, virtual, *sequences)
#   - event_generate(self, sequence, **kw)
#   - event_info(self, virtual=None)
#   - focus = focus_set(self)
#   - focus_displayof(self)
#   - focus_force(self)
#   - focus_get(self)
#   - focus_lastfor(self)
#   - focus_set(self)
#   - getboolean(self, s)
#   - getvar(self, name='PY_VAR')
#   - grab_current(self)
#   - grab_release(self)
#   - grab_set(self)
#   - grab_set_global(self)
#   - grab_status(self)
#   - grid_anchor(self, anchor=None)
#   - grid_bbox(self, column=None, row=None, col2=None, row2=None)
#   - grid_columnconfigure(self, index, cnf={}, **kw)
#   - grid_location(self, x, y)
#   - grid_propagate(self, flag=['_noarg_'])
#   - grid_rowconfigure(self, index, cnf={}, **kw)
#   - grid_size(self)
#   - grid_slaves(self, row=None, column=None)
#   - image_names(self)
#   - image_types(self)
#   - keys(self)
#   - lift = tkraise(self, aboveThis=None)
#   - lower(self, belowThis=None)
#   - mainloop(self, n=0)
#   - nametowidget(self, name)
#   - option_add(self, pattern, value, priority=None)
#   - option_clear(self)
#   - option_get(self, name, className)
#   - option_readfile(self, fileName, priority=None)
#   - pack_propagate(self, flag=['_noarg_'])
#   - pack_slaves(self)
#   - place_slaves(self)
#   - propagate = pack_propagate(self, flag=['_noarg_'])
#   - quit(self)
#   - register = _register(self, func, subst=None, needcleanup=1)
#   - rowconfigure = grid_rowconfigure(self, index, cnf={}, **kw)
#   - selection_clear(self, **kw)
#   - selection_get(self, **kw)
#   - selection_handle(self, command, **kw)
#   - selection_own(self, **kw)
#   - selection_own_get(self, **kw)
#   - send(self, interp, cmd, *args)
#   - setvar(self, name='PY_VAR', value='1')
#   - size = grid_size(self)
#   - slaves = pack_slaves(self)
#   - tk_bisque(self)
#   - tk_focusFollowsMouse(self)
#   - tk_focusNext(self)
#   - tk_focusPrev(self)
#   - tk_menuBar(self, *args)
#   - tk_setPalette(self, *args, **kw)
#   - tk_strictMotif(self, boolean=None)
#   - tkraise(self, aboveThis=None)
#   - unbind(self, sequence, funcid=None)
#   - unbind_all(self, sequence)
#   - unbind_class(self, className, sequence)
#   - update(self)
#   - update_idletasks(self)
#   - wait_variable(self, name='PY_VAR')
#   - wait_visibility(self, window=None)
#   - wait_window(self, window=None)
#   - waitvar = wait_variable(self, name='PY_VAR')
#   - winfo_atom(self, name, displayof=0)
#   - winfo_atomname(self, id, displayof=0)
#   - winfo_cells(self)
#   - winfo_children(self)
#   - winfo_class(self)
#   - winfo_colormapfull(self)
#   - winfo_containing(self, rootX, rootY, displayof=0)
#   - winfo_depth(self)
#   - winfo_exists(self)
#   - winfo_fpixels(self, number)
#   - winfo_geometry(self)
#   - winfo_height(self)
#   - winfo_id(self)
#   - winfo_interps(self, displayof=0)
#   - winfo_ismapped(self)
#   - winfo_manager(self)
#   - winfo_name(self)
#   - winfo_parent(self)
#   - winfo_pathname(self, id, displayof=0)
#   - winfo_pixels(self, number)
#   - winfo_pointerx(self)
#   - winfo_pointerxy(self)
#   - winfo_pointery(self)
#   - winfo_reqheight(self)
#   - winfo_reqwidth(self)
#   - winfo_rgb(self, color)
#   - winfo_rootx(self)
#   - winfo_rooty(self)
#   - winfo_screen(self)
#   - winfo_screencells(self)
#   - winfo_screendepth(self)
#   - winfo_screenheight(self)
#   - winfo_screenmmheight(self)
#   - winfo_screenmmwidth(self)
#   - winfo_screenvisual(self)
#   - winfo_screenwidth(self)
#   - winfo_server(self)
#   - winfo_toplevel(self)
#   - winfo_viewable(self)
#   - winfo_visual(self)
#   - winfo_visualid(self)
#   - winfo_visualsavailable(self, includeids=0)
#   - winfo_vrootheight(self)
#   - winfo_vrootwidth(self)
#   - winfo_vrootx(self)
#   - winfo_vrooty(self)
#   - winfo_width(self)
#   - winfo_x(self)
#   - winfo_y(self)
#
# ------------------------------------------------------------------------
# |  Data descriptors inherited from Misc:
# |  
#   - __dict__
#   - __weakref__
#
# |  ----------------------------------------------------------------------
# |  Data and other attributes inherited from Misc:
# | 
#   - getdouble = <class 'float'>
#   - getint = <class 'int'>
#
# |  ----------------------------------------------------------------------
# |  Methods inherited from Wm:
# | 
#   - aspect = wm_aspect(self, minNumer=None, minDenom=None, maxNumer=None, maxDenom=None)
#   - attributes = wm_attributes(self, *args)
#   - client = wm_client(self, name=None)
#   - colormapwindows = wm_colormapwindows(self, *wlist)
#   - command = wm_command(self, value=None)
#   - deiconify = wm_deiconify(self)
#   - focusmodel = wm_focusmodel(self, model=None)
#   - forget = wm_forget(self, window)
#   - frame = wm_frame(self)
#   - geometry = wm_geometry(self, newGeometry=None)
#   - grid = wm_grid(self, baseWidth=None, baseHeight=None, widthInc=None, heightInc=None)
#   - group = wm_group(self, pathName=None)
#   - iconbitmap = wm_iconbitmap(self, bitmap=None, default=None)
#   - iconify = wm_iconify(self)
#   - iconmask = wm_iconmask(self, bitmap=None)
#   - iconname = wm_iconname(self, newName=None)
#   - iconphoto = wm_iconphoto(self, default=False, *args)
#   - iconposition = wm_iconposition(self, x=None, y=None)
#   - iconwindow = wm_iconwindow(self, pathName=None)
#   - manage = wm_manage(self, widget)
#   - maxsize = wm_maxsize(self, width=None, height=None)
#   - minsize = wm_minsize(self, width=None, height=None)
#   - overrideredirect = wm_overrideredirect(self, boolean=None)
#   - positionfrom = wm_positionfrom(self, who=None)
#   - protocol = wm_protocol(self, name=None, func=None)
#   - resizable = wm_resizable(self, width=None, height=None)
#   - sizefrom = wm_sizefrom(self, who=None)
#   - state = wm_state(self, newstate=None)
#   - title = wm_title(self, string=None)
#   - transient = wm_transient(self, master=None)
#   - withdraw = wm_withdraw(self)
#   - wm_aspect(self, minNumer=None, minDenom=None, maxNumer=None, maxDenom=None)
#   - wm_attributes(self, *args)
#   - wm_client(self, name=None)
#   - wm_colormapwindows(self, *wlist)
#   - wm_command(self, value=None)
#   - wm_deiconify(self)
#   - wm_focusmodel(self, model=None)
#   - wm_forget(self, window)
#   - wm_frame(self)
#   - wm_geometry(self, newGeometry=None)
#   - wm_grid(self, baseWidth=None, baseHeight=None, widthInc=None, heightInc=None)
#   - wm_group(self, pathName=None)
#   - wm_iconbitmap(self, bitmap=None, default=None)
#   - wm_iconify(self)
#   - wm_iconmask(self, bitmap=None)
#   - wm_iconname(self, newName=None)
#   - wm_iconphoto(self, default=False, *args)
#   - wm_iconposition(self, x=None, y=None)
#   - wm_iconwindow(self, pathName=None)
#   - wm_manage(self, widget)
#   - wm_maxsize(self, width=None, height=None)
#   - wm_minsize(self, width=None, height=None)
#   - wm_overrideredirect(self, boolean=None)
#   - wm_positionfrom(self, who=None)
#   - wm_protocol(self, name=None, func=None)
#   - wm_resizable(self, width=None, height=None)
#   - wm_sizefrom(self, who=None)
#   - wm_state(self, newstate=None)
#   - wm_title(self, string=None)
#   - wm_transient(self, master=None)
#   - wm_withdraw(self)
#
"""

# -----------------------------------------------------------------------------
root.resizable(width=False, height=False)


root.mainloop()

## ----------------------------------------------------------------------------